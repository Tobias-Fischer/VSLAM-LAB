import os.path
import subprocess
from zipfile import ZipFile
from huggingface_hub import hf_hub_download

from utilities import print_msg
from path_constants import VSLAMLAB_BASELINES
from Baselines.BaselineVSLAMLab import BaselineVSLAMLab
from utilities import ws, print_msg

SCRIPT_LABEL = f"\033[95m[{os.path.basename(__file__)}]\033[0m "

class DVSEVO_baseline(BaselineVSLAMLab):
    def __init__(self, baseline_name='dvsevo', baseline_folder='DVSEVO'):

        default_parameters = {'verbose': 1, 'mode': 'mono'}
        
        # Initialize the baseline
        super().__init__(baseline_name, baseline_folder, default_parameters)
        self.color = 'green'
        self.modes = ['mono']

    def build_execute_command(self, exp_it, exp, dataset, sequence_name):
        vslamlab_command = f"pixi run --frozen -e {self.baseline_name} execute_mono " + f'{sequence_name}.launch'
        return vslamlab_command

    # def execute(self, command, exp_it, exp_folder, timeout_seconds=1*60*1000000):
    #     log_file_path = os.path.join(exp_folder, "system_output_" + str(exp_it).zfill(5) + ".txt")
    #     comments = ""
    #     #comment_queue = queue.Queue()
    #     success_flag = [True] 
    #     memory_stats = {}
    #     with open(log_file_path, 'w') as log_file:
    #         print(f"{ws(8)}log file: {log_file_path}")
    #         #process = subprocess.Popen(command, shell=True, stdout=log_file, stderr=log_file, text=True, preexec_fn=os.setsid)
    #         print(command)
    #         subprocess.run(command, shell=True)

    #         #memory_thread = threading.Thread(target=self.monitor_memory, args=(process, 10, comment_queue, success_flag, memory_stats))
    #         #memory_thread.start()

    #         # try:
    #         #     _, _ = process.communicate(timeout=timeout_seconds)
    #         # except subprocess.TimeoutExpired:
    #         #     print_msg(SCRIPT_LABEL, f"Process took too long > {timeout_seconds} seconds",'error')
    #         #     comments = f"Process took too long > {timeout_seconds} seconds. Process killed."
    #         #     success_flag[0] = False
    #         #     self.kill_process(process)
            
    #         #memory_thread.join()
    #         #while not comment_queue.empty():
    #         #    comments += comment_queue.get() + "\n"

    #     #if not os.path.exists(os.path.join(exp_folder, str(exp_it).zfill(5) + f"_{TRAJECTORY_FILE_NAME}.txt" )):
    #         #success_flag[0] = False

    #     return {
    #         "success": success_flag[0],
    #         "comments": comments,
    #         "ram": memory_stats.get('ram', 'N/A'),
    #         "swap": memory_stats.get('swap', 'N/A'),
    #         "gpu": memory_stats.get('gpu', 'N/A')
    #     }

    def is_cloned(self):
        return os.path.isdir(os.path.join(self.baseline_path, 'catkin_ws', 'src', 'rpg_dvs_evo_open'))
        
    def is_installed(self): 
        return (True, 'is installed') if self.is_cloned() else (False, 'not installed (conda package available)')
    
class DVSEVO_baseline_dev(DVSEVO_baseline):
    def __init__(self):
        super().__init__(baseline_name = 'dvsevo-dev', baseline_folder =  'DVSEVO-DEV')

    def is_installed(self):
        is_installed = os.path.isfile(os.path.join(self.baseline_path, 'catkin_ws', 'devel', 'bin', 'rqt_evo'))
        return (True, 'is installed') if is_installed else (False, 'not installed (auto install available)')
        
