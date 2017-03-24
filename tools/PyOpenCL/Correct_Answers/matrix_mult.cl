__kernel void mmul(
	const int N,
	__global float* A,
	__global float* B,
	__global float* C)
{
    int i = get_global_id(0);
    int j = get_global_id(1);
    int k;
    for (k = 0; k < N; k++) {
        C[i*N+j] += A[i*N+k] * B[k*N+j];
    }
        
}