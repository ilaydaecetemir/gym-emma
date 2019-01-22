import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='Emma-v0',
    entry_point='gym_emma.envs:EmmaEnv',
    #timestep_limit=1000,
    #reward_threshold=2.0,
    #nondeterministic = True,
)

