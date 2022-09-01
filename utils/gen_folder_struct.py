from pathlib import Path
import shutil 

def refactor_path(path: Path):
    name = path.name
    name = name.lower().replace('(', '').replace(')', '').replace(' ', '_').replace('-', 'or').replace(',', '')
    if name.endswith('_'):
        name = name[:-1] + ''
    return name

for path in Path('./assets/').rglob('*'):
    new_path = refactor_path(path)
    print(f'{path.name} -> {new_path}')
    path = path.rename(path.with_name(new_path))
    absolute = path.absolute().as_posix()
    local_path = absolute.split('icons', 1)[1]
    
    if(local_path.__contains__('icons')):
        if(absolute.endswith('data.json')):
            shutil.copy(path.as_posix(), f'./{path.parents[1]}_lottie.json')
        if(absolute.endswith('.svg')):
            shutil.copy(path.as_posix(), f'./{path.parents[1]}.svg')
    elif(absolute.__contains__('loaders') & absolute.endswith('data.json')):
            shutil.copy(path.as_posix(), f'./{path.parents[1]}_lottie.json')
