import numpy as np
import gym 

env= gym.make('FrozenLake-v0')

n=env.action_space.n
m=env.observation_space

print(n)
print(m)

q=np.zeros((3,2))
V=np.zeros(m)

gamma=0.99
the=1e-2
max_episode=10000

for i in range(max_episode):
	v_ep=np.copy(V)
	env.reset()
	for i in range(m):
		k=[]
		for a in range(n):
			val=0
			for p,s_,r,_ in env.env.P[i][a]:
				val+=p*(r+gamma* v_ep[s_])
			k.append(val)
		V[i]=np.max(k)
	if max(V-v_ep)<the:
		print('Done training !')
		break

#print(q)
s=env.reset()
rewards=[]
for i in range(10000):
	s=env.reset()
	d=False
	R=0
	while d==False:
		a=np.argmax([sum([p*(r+gamma*V[s_]) for p,s_,r,_ in env.env.P[s][j]]) for j in range(n)])
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