import shutil
import os.path

paths=[
"~/.bashrc",
"~/.config/git/git-completion.sh",
"~/.config/git/git-prompt.sh",
"~/.config/alacritty",
"~/.config/git",
"~/.config/qtile",
"~/.config/qutebrowser"]

home_path = os.path.expanduser('~')

for i in paths:
    
    if "~" in i:
        final_path = i.split('~')
        whole_path = home_path+final_path[-1]
        
        dirs = i.split('/')[1:-1]
        dirs_path = ''
        for j in dirs:
            dirs_path = dirs_path + j + '/'

        if os.path.isdir(whole_path):
            try:
                shutil.rmtree(os.getcwd()+'/'+dirs_path+os.path.split(i)[-1])
            except:
                print("Dir not found, copying...")
            
            shutil.copytree(whole_path,os.getcwd()+'/'+dirs_path+os.path.split(i)[-1])
        else:
            print(whole_path)
            shutil.copy(whole_path,os.getcwd()+'/'+dirs_path+os.path.split(i)[-1])


