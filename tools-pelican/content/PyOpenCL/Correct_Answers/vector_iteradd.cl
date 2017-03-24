#define ITER 16

__kernel void vadd(
    __global float* a,
    __global float* b,
    __global float* c,
    const unsigned int count)
{
    int i = get_global_id(0) * ITER;
    int j;
    
    for (j = 0; j < ITER; j++) {
    	/* c[i*ITER+j] = a[i*ITER+j] + b[i*ITER+j]; */
	c[i+j] = a[i+j] + b[i+j];
    }

}