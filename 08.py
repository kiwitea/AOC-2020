import runner
from pathlib import Path


def part1(data):
    commands = dict(enumerate(data.splitlines()))
    
    acc = 0
    current_idx = 0
    
    emergency_brake = 1000
    
    while emergency_brake > 0:
        try:
            cmd = commands.pop(current_idx)
        except KeyError:
            print(f'Command {current_idx} already ran.')
            break
        
        if cmd.startswith('acc'):
            acc += int(cmd.split(' ')[1])
            current_idx += 1
        elif cmd.startswith('jmp'):
            current_idx += int(cmd.split(' ')[1])
        else:
            current_idx += 1
            
        emergency_brake -= 1
        
    return acc

class TheEnd(Exception):
    
    def __init__(self, acc: int, *args: object) -> None:
        super().__init__(*args)
        self.acc = acc
        

def run(commands: dict, current_idx: int, exit_idx: int, primary: bool = True) -> int:
    emergency_brake = 1000
    acc = 0
    
    while emergency_brake > 0:
        try:
            cmd = commands.pop(current_idx)
            parameter = int(cmd.split(' ')[1])
        except KeyError:
            raise KeyError(f'You hit an infinite loop.')
        
        if cmd.startswith('acc'):
            acc += parameter
            current_idx += 1
        elif cmd.startswith('jmp'):
            
            if primary:
                # allowed to change 1 command
            
                if (current_idx + 1) == exit_idx:
                    print(f'Changing L{current_idx} "{cmd}" to noop ends the loop.')
                    raise TheEnd(acc=acc)
                
                # add run path: if this was a noop
                try:
                    print(f'Create run path from L{current_idx}')
                    acc += run(commands.copy(), current_idx + 1, exit_idx, primary=False)
                    print(f'Run path completed from L{current_idx}: ACC = {acc}')
                except KeyError:
                    # nope, still an infinite loop
                    print('nice try')
                    pass
                except TheEnd as end:
                    # Run path hit the end of instruction. This is good.
                    print(f'Hit the end in run path L{current_idx}: ACC = {acc} + {end.acc} => {acc+end.acc}')
                    raise TheEnd(acc=acc + end.acc)
                
            else:
                # not allowed to change another cmd
                pass
            
            current_idx += parameter  # JMP +/- X
        else:
            # check if we could exit if this was a jmp
            if primary and (current_idx + parameter) == exit_idx:
                print(f'Found it. Changed L{current_idx} "{cmd}" to "jmp {parameter}".')
                return acc
            current_idx += 1
            
        if current_idx == exit_idx:
            print('Reached the end')
            raise TheEnd(acc=acc)
            
        emergency_brake -= 1
        
    if emergency_brake == 0:
        raise RuntimeError('Emergency break.')
        
    return acc
        
    


def part2(data):
    command_list = data.splitlines()
    commands = dict(enumerate(command_list))
    exit_idx = len(command_list)
        
    try:
        acc = run(commands, 0, exit_idx)
    except TheEnd as end:
        print(end)
        acc = end.acc
        
    return acc


runner.run(day=int(Path(__file__).stem))