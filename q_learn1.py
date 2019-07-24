import numpy as np
import gym 
import random

env= gym.make('Taxi-v2')

n=env.action_space.n
m=env.observation_space.n

q=np.zeros((m,n))

gamma=0.99
the=1e-2
max_episode=10000
alpha=0.8
eps=0.8

for i in range(max_episode):
	if max_episode> 1000:
		alpha=0.2
		eps=0.2

	q_ep=np.copy(q)
	env.reset()
	for i in range(m):
		ran=random.random()
		s_=-1
		r=0
		
		if ran< eps:
			a=random.randint(0,n-1)
			[(_,s_,r,_)]= env.env.P[i][a]
		else:
			a=np.argmax(q[i,:])
			[(_,s_,r,_)]= env.env.P[i][a]
		
		q[i,a]= (1-alpha) * q[i,a] + alpha * (r + gamma* np.max(q[s_,:]))
	
print('training done')



s=env.reset()
d=False
R=0
while d==False:
	a=np.argmax(q[s,])
	input()
	env.render()
	s2,r,d,_=env.step(a)
	print(R)
	R=R*gamma+r
	s=s2

print("Final:"),
print(r)



