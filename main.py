#import dominoEnv
import gym
import gym_domino
env = gym.make('Domino-v0')

#env = dominoEnv.DominoEnv(edset = "d6")
env.reset()
print(env.action_space)
print(env.observation_space)
print(env.state)

for j in range(100):
    env.reset()
    done = False
    rew = 0
    vals = []
    for i in range(29):
        vals.append(0)
    while(not done):
        vv,vi,pq = env._valid_actions(vals)
        print pq
        a,rew,done,b = env.step(pq[0])
    #print env.valid_actions(vals)

#
#    action = firstplay = random.randint(0,29)
#    _,rew,done,_ = env._step(action)