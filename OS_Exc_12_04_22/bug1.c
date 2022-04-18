/******************************************************************************
* FILE: bug1.c
* DESCRIPTION:
*   This example has a bug. It is a variation on the condvar.c example. 
*   Instead of just one thread waiting for the condition signal, there are
*   four threads waiting for the same signal. Find out how to fix the
*   program. The solution program is bug1fix.c.
* SOURCE: Adapted from example code in "Pthreads Programming", B. Nichols
*   et al. O'Reilly and Associates.
* LAST REVISED: 07/06/05  Blaise Barney
******************************************************************************/
#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h> 
#define NUM_THREADS  6
#define TCOUNT 10
#define COUNT_LIMIT 12

int     count = 0;
pthread_mutex_t count_mutex;
pthread_cond_t count_threshold_cv;
time_t start,end; 
void *inc_count(void *idp) 
{
  int j,i;
  double result=0.0;
  long my_id = (long)idp;
  for (i=0; i < TCOUNT; i++) {
    pthread_mutex_lock(&count_mutex);
    /* 
    Check the value of count and signal waiting thread when condition is
    reached.  Note that this occurs while mutex is locked. 
    */
    if (count == COUNT_LIMIT) {
          pthread_cond_broadcast(&count_threshold_cv);
    printf("inc_count(): thread %ld, count = %d  Threshold reached.\n", my_id, count);
    }
          ++count;
                      printf("inc_count(): thread %ld, count = %d, unlocking mutex\n", my_id, count);
    pthread_mutex_unlock(&count_mutex);

    /* Do some work so threads can alternate on mutex lock */
    sleep(1);
    }
  pthread_exit(NULL);
}

void *watch_count(void *idp) 
{
  long my_id = (long)idp;

  printf("Starting watch_count(): thread %ld\n", my_id);

  /*
  Lock mutex and wait for signal.  Note that the pthread_cond_wait routine
  will automatically and atomically unlock mutex while it waits. 
  Also, note that if COUNT_LIMIT is reached before this routine is run by
  the waiting thread, the loop will be skipped to prevent pthread_cond_wait
  from never returning.
  */
  pthread_mutex_lock(&count_mutex);
    printf("***Before cond_wait: thread %ld\n", my_id);
    pthread_cond_wait(&count_threshold_cv, &count_mutex);
    printf("***Thread %ld Condition signal received.\n", my_id);
  pthread_mutex_unlock(&count_mutex);
  pthread_exit(NULL);
}

int main(int argc, char *argv[])
{
srand(time(NULL)); 
  int i, rc;
  pthread_t threads[NUM_THREADS];
  pthread_attr_t attr;

  /* Initialize mutex and condition variable objects */
  pthread_mutex_init(&count_mutex, NULL);
  pthread_cond_init (&count_threshold_cv, NULL);
	start = clock(); 
  /*
  For portability, explicitly create threads in a joinable state 
  */
  pthread_attr_init(&attr);
  pthread_attr_setdetachstate(&attr, PTHREAD_CREATE_JOINABLE);
	for (i = 2; i < NUM_THREADS; ++i)
	{
	pthread_create(&threads[i], &attr, watch_count, (void *)i); 
	}
  pthread_create(&threads[0], &attr, inc_count, (void *)0);
 pthread_create(&threads[1], &attr, inc_count, (void *)1);

  /* Wait for all threads to complete */
  for (i = 0; i < NUM_THREADS; i++) {
    pthread_join(threads[i], NULL);
  }
  printf ("Main(): Waited on %d  threads. Done.\n", NUM_THREADS);
 end = clock(); 
    	    	double exe_time = ((double)(end - start)) / ( (double)(CLOCKS_PER_SEC) ); 
    	printf("Time: %g seconds\n", exe_time);
  /* Clean up and exit */
  pthread_attr_destroy(&attr);
  pthread_mutex_destroy(&count_mutex);
  pthread_cond_destroy(&count_threshold_cv);
  pthread_exit (NULL);

}
