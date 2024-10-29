import numpy as jp

p = jp.array([[2.0, 3.0, 4.0],[5.0, 6.0,7.0]])
print (p)
print(p.ndim)
print(p.shape)
print(p.dtype)
q = jp.array([[2.0, 3.0, 4.0],[5.0, 6.0,7.0]], dtype = 'int16')
print(q.dtype)
print (q)

'''m = jp.array([[1, 2, 3, 4, 5, 6],[7, 8, 9, 10, 11]])
print(m[1, 1:5:2])'''

x = jp.array([[[6,9],[6,9]],[[4,4],[2,4]]])
print(x)
x [0,1,:] =[4,5]
print(x)

print(jp.zeros((3,3,3)))
print(jp.full((3,3,3,),3,dtype='float'))
print(jp.full(p.shape, 123))
print(jp.full_like(p, 123))
print(jp.random.rand(2,3,3))
print(jp.random.random_sample(p.shape))
print(jp.random.randint(69, size=(2,4)))
print(jp.identity(5))

frr = jp.array([[2,5,8]])
fff = jp.repeat(frr,3, axis= 1)
print(fff)

kk = jp.full((5,5),9, dtype='int32')
fk = jp.zeros((3,3))
fk[1,1] = 1
kk[1:4, 1:4] = fk
print(kk)

a = jp.ones((2,3))
b= jp.full((3,2),4)
print(jp.matmul(a,b))

res = q.reshape(3,2)
print(res)
print(jp.vstack((p,q)))
print(jp.hstack((p,q)))
