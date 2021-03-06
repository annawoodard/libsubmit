template_string = '''#!/bin/bash
Universe = vanilla

Executable = $user_script

Output = $submit_script_dir/${jobname}.out.$$(Cluster).$$(Process)
Error = $submit_script_dir/${jobname}.err.$$(Cluster).$$(Process)
Log = $submit_script_dir/${jobname}.$$(Cluster)

leave_in_queue = true

request_cpus = $tasks_per_node

$condor_overrides

queue $nodes
'''


template_string = '''
universe                = vanilla
should_transfer_files   = YES
when_to_transfer_output = ON_EXIT_OR_EVICT
Transfer_Executable     = false
transfer_input_files    = ${input_files}
machine_count           = ${nodes}
output                  = ${submit_script_dir}/${job_name}.stdout
error                   = ${submit_script_dir}/${job_name}.stderr
executable              = /bin/bash
arguments               = ${job_script}
requirements            = ${requirements}
projectname             = ${project}
leave_in_queue          = TRUE

${condor_overrides}

queue

'''

# for later, 
# if we want to remove on preemption, this might work:
#    PERIODIC_REMOVE = (NumJobstarts > 1)
# or if the pilot can trap signals, then we can send a special exit code on
# sigterm/sigkill and remove that way. but then we still need to be careful in
# cases where the worker dies, for example-- no signal is sent
