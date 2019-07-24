import gym
import numpy as np
import random
import math

env = gym.make('MountainCar-v0')

n=env.action_space.n
state_range=list(zip(env.observation_space.low,env.observation_space.high))

states_space=(50,10)

q_table=np.zeros(states_space + (n,))

gamma=0.99
streak=0
max_episode=3000
alpha=0.8
eps=0.8
time=200
passing=100

def state_map(state):
	index = []
	for i in range(len(states_space)):
		if state[i] <= state_range[i][0]:
			ind=0
		elif state[i] >= state_range[i][1]:
			ind=states_space[i]-1
		else:
			small=state_range[i][1] - state_range[i][0]
			small=small/states_space[i]
			ind=(state[i]-state_range[i][0])
			ind=ind/small
			ind=(int)(ind)
		index.append(ind)
	return tuple(index)

for i in range(max_episode):
	if i > max_episode/4:
		alpha=0.1
		eps=0.1
	ob=env.reset()
	s=state_map(ob)
	max_time=200
	for t in range(max_time):
		env.render()
		ran=random.random()
		if ran< eps:
			a=random.randint(0,n-1)
		else:
			a=np.argmax(q_table[s])
		ob2,reward,done,_ = env.step(a)
		s2= state_map(ob2)
		q_table[s+(a,)]= (1-alpha)*q_table[s+(a,)] + alpha* (reward+ gamma*np.max(q_table[s2]))
		s=s2
		if done or max_time==249:
			break
	if t<199:
		streak+=1
	else:
		streak=0
	print("Episode %d finished after %d time steps with a streak of %d" % (i, t, streak))
	if streak>10:
		print("Finished training!")
		break
print(q_table)

print("Final evaluation press enter")
input()


d=False
R=0
rewards=[]
for i in range(4):
	obs=env.reset()
	s=state_map(obs)
	d=False
	R=0
	while d==False :
		a=np.argmax(q_table[s])
		env.render()
		obs2,r,d,_=env.step(a)
		s2=state_map(obs2)
		R=R+r
		s=s2
		if d:
			print(r)
			rewards.append(R)
			break
print(np.mean(rewards))	

env.close()








