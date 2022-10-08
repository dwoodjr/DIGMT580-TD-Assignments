import os, sys

'''
This script creates a file directory on the system 
and sets the created directory as the new value
for an environment variable set through DOSKEY 
'''
try:
    cwd = os.getcwd()
    #print(cwd)
    
    #set variables
    env_var = os.environ.get('asset')
    env_var_value = 'assets/{}/maya/scenes'.format(str(env_var))
    path = os.path.join('E:/OneDrive - Drexel University/DIGM T580 FA 22_TD/GitHub/anim-t380-assignments/assignment-3/bin', env_var_value)
    
    #function to set the environment variable value
    def set_env():
        os.environ[env_var] = path
        os.system('SETX {0} "{1}"'.format(str(env_var),str(path)))
        print('Environment variable {} has been set to {}'.format(str(env_var),str(path)))
        
    #function to create a file directory        
    def create_dir(): 
        os.makedirs(env_var)
        print('A Directory has been created: {}'.format(str(env_var)))
        
    #print(env_var)
    
    create_dir()    
    set_env()
    

except KeyError:
    print('Need to define the environment variable')
    sys.exit(1)

