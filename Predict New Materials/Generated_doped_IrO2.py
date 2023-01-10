from pymatgen.core import Structure, Lattice
from pymatgen.core import Molecule
from pymatgen.analysis.adsorption import *
from pymatgen.core.surface import generate_all_slabs
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
from pymatgen.ext.matproj import MPRester
from pymatgen.io.vasp.inputs import Poscar
from pymatgen.io.vasp.inputs import Kpoints
from pymatgen.io.vasp.inputs import Incar
from pymatgen.io.vasp.inputs import Potcar
from pymatgen.io.vasp.inputs import PotcarSingle
from pymatgen.io.vasp.sets import MPRelaxSet
from pymatgen.ext.matproj import MPRester
my_key='BJU2qDd4gpCPO0rf'
m= MPRester(my_key)
import random
slab_basic=Structure.from_file('IrO2_110_init.cif')
def substitue_slab(ele_list,sub_list,slab):
    slab_copied=slab.copy()
    for i in range(0,len(ele_list)):
        ele_each=ele_list[i]
        sub_each=sub_list[i]
        slab_copied[sub_each]=ele_each
    return slab_copied
def mkdir(path): 
    folder = os.path.exists(path) 
    if not folder:
        os.makedirs(path)
        print ("---  new folder...  ---")
        print ("---  OK  ---") 
    else:
        print ("---  There is this folder!  ---")
ele_list=['Sc','V','Eu','Cu','Pt','Au']
for i in range(1,1000):
    random.seed(i)
    replaced_serial_list=random.sample(range(0,40),6)
    replaced_slab=substitue_slab(ele_list,replaced_serial_list,slab_basic)
    path='./the_'+str(i)+'_th_structure/'
    mkdir('the_'+str(i)+'_th_structure')
    try:
        open(path+'POSCAR','w').write(str(Poscar(replaced_slab,sort_structure=True)))
    except:
        print('do not exist')
    mpr=MPRelaxSet(replaced_slab)
    mpr.write_input(output_dir=path)