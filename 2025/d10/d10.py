from typing import List
from math import inf
import copy

class LightCmd:

    def __init__(self, cmds: List[str]):
        self.light_count, self.light_state, self.exp_light_state = LightCmd._parse_light(cmds[0])
        self.init_light_state = copy.deepcopy(self.light_state)
        self.actions = LightCmd._parse_cmds(cmds[1:-1])
        self.jol_req = LightCmd._parse_jol_req(cmds[-1])
        self.min_steps = len(self.actions)

    @staticmethod
    def _parse_light(lights: str):
        light_count = 0
        exp_light_state = []
        init_light_state = []
        for light in list(lights[1:-1]):
            if light == ".":
                exp_light_state.append(False)
            else:
                exp_light_state.append(True)
            init_light_state.append(False)
            light_count += 1
        return light_count, init_light_state, exp_light_state

    @staticmethod
    def _parse_cmds(cmds: List[str]):
        cmds_list = []
        for cmd in cmds:
            light_idxs = cmd[1:-1].split(",")
            light_idxs = list(map(lambda idx_str: int(idx_str), light_idxs))
            cmds_list.append(light_idxs)

        return cmds_list

    @staticmethod
    def _parse_jol_req(joltage_req_str: str):
        jol_req = joltage_req_str[1:-1].split(",")
        jol_req = list(map(lambda idx_str: int(idx_str), jol_req))
        return jol_req

    def flip_light(self, action: List[int]):
        for idx in action:
            self.light_state[idx] = not self.light_state[idx]

    def is_light_state_expected(self):
        return self.light_state == self.exp_light_state

    def _reset_light_state(self):
        for i in range(self.light_count):
            self.light_state[i] = self.init_light_state[i]

    def _print_actions(self, steps: int):
        # print("steps takes", steps)
        print(self.actions[:steps])

    def _permutate_all_actions(self, start: int, end: int, steps: int):
        if start == end or steps > self.min_steps:
            return True

        for i in range(start, end):
            if steps > self.min_steps:
                break

            self.actions[start], self.actions[i] = self.actions[i], self.actions[start]
            self.flip_light(self.actions[start])

            to_stop = False
            if (self.exp_light_state == self.light_state):
                self.min_steps = min(self.min_steps, steps)
                to_stop = True
            else:
                self._permutate_all_actions(start + 1, end, steps + 1)

            self.flip_light(self.actions[start])
            self.actions[start], self.actions[i] = self.actions[i], self.actions[start]

            if to_stop:
                break

    def find_min_steps(self):
        self.min_steps = len(self.actions)
        self._permutate_all_actions(0, len(self.actions), 1)
        return self.min_steps

    def run_actions(self, steps):
        self._print_actions(steps)
        for action in self.actions[:steps]:
            self.flip_light(action)

        res = self.light_state == self.exp_light_state
        self._reset_light_state()
        return res

if __name__ == "__main__":
    light_cmds = []
    with open("D:\\local_repo\\AOC\\2025\\d10\\input_Test.txt", "r") as f:
        for line in f:
            cmds = line.rstrip("\n").split(" ")
            light_cmds.append(LightCmd(cmds))


    total_sum = 0

    for l in light_cmds:
        # print("light_count", l.light_count)
        # print("exp_light_state", l.exp_light_state)
        # print("actions", l.actions)
        steps = l.find_min_steps()
        print("actions", steps)
        total_sum += steps

    print(total_sum)