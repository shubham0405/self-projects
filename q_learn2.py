import numpy as np
import gym 
import random

env= gym.make('FrozenLake-v0')

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
		
		if ran< eps:
			a=random.randint(0,n-1)	
		else:
			a=np.argmax(q[i,:])
		q[i,a]= (1-alpha) * q[i,a]
		for p,s_,r,_ in env.env.P[i][a]:
			q[i,a] += p*alpha * (r + gamma* np.max(q[s_,:]))
        	

print('training done')

#print(q)

s=env.reset()
rewards=[]
for i in range(10000):
	s=env.reset()
	d=False
	R=0
	while d==False:
		a=np.argmax(q[s,])
		#input()
		#env.render()
		s2,r,d,_=env.step(a)
		#print(R)
		R=R*gamma+r
		s=s2
		if d:
			rewards.append(r)
			break
print(np.mean(rewards))	


