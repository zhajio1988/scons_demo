import os

def find_sources(directory, extensions, depth=0):
    """
    Find files with given extensions up to a specified depth in the directory.

    :param directory: The root directory to start searching.
    :param extensions: A tuple of file extensions to look for.
    :param depth: The depth of directory traversal (0 for unlimited, 1 for first level, 2 for two levels, etc.)
    :return: A list of paths to files with the specified extensions.
    """
    sources = []

    # Check depth 0 case for unlimited depth
    if depth == 0:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(extensions):
                    sources.append(os.path.join(root, file))
    else:
        # For depth > 0, we need to limit the directory traversal
        for root, dirs, files in os.walk(directory):
            # Calculate the current depth of the directory
            current_depth = root[len(directory):].count(os.sep)

            # Add files if we are within the allowed depth
            if current_depth < depth:
                for file in files:
                    if file.endswith(extensions):
                        sources.append(os.path.join(root, file))
            # Remove subdirectories from the list to prevent further traversal
            if current_depth == depth - 1:
                dirs[:] = []

    return sources

def get_path_files(dirs, file_ext):
    path_files = []
    # print('dir: ' + str(dirs))
    for dir in dirs:
        # print('dir: ' + dir)
        path_files.append(Glob(dir + '/' + file_ext))
    return path_files


GCC_riscv_PATH = '/opt/picocom/ThirdParty_Libs/T-head/C920_R2S0P21/C920_R2S0_manuals_and_tools/manuals_and_tools/08_toolchain_900_series_cpu_toolchain/V2.8.0/Xuantie-900-gcc-elf-newlib-x86_64-V2.8.0/bin/'

#PLF = 'riscv'
PLF = 'riscv'

# toolchains
if PLF == 'riscv':
    PREFIX = GCC_riscv_PATH + 'riscv64-unknown-elf-'
else:
    PREFIX = ''

CC      = PREFIX + 'gcc'
CXX     = PREFIX + 'g++'
AS      = PREFIX + 'as'
AR      = PREFIX + 'ar'
LINK    = PREFIX + 'gcc'
RANLIB  = PREFIX + 'ranlib',

SIZE = PREFIX + 'size'
OBJDUMP = PREFIX + 'objdump'
OBJCPY = PREFIX + 'objcopy'

TARGET_PATH = 'build/'
TARGET_NAME = 'main'
TARGET_WITHOUT_SUFFIX = TARGET_PATH + TARGET_NAME


###################################################################################
# C source dirs config
C_DIRS = ['lib/clib/', 'lib/newlib_wrap/']
#C_DIRS.append('src')

# C source files config
C_FILES = ['hello_world.c']
#C_FILES.append('main.c')

# Create c sources list
C_SRC_LIST = get_path_files(C_DIRS, '*.c') + C_FILES


###################################################################################
# ASM source dirs config
AS_DIRS = []
#AS_DIRS.append('src')

# ASM source files config
AS_FILES = []
#AS_FILES.append('startup.s')

AS_SRC_LIST = get_path_files(AS_DIRS, '*.s') + AS_FILES


###################################################################################
# -I, Include path config
CPP_PATH = ['lib/init', 'lib/clib/', 'lib/newlib_wrap/']
#CPP_PATH.append('inc')

# -D, Preprocess Define
CPP_DEFINES = []
#CPP_DEFINES.append('CFG_TEST')

# C generate define
C_FLAGS = []
#C_FLAGS.append('-O1')
#C_FLAGS.append('-g')
C_FLAGS.append('-mtune=c920 -march=rv64imafdcv_zicbom_zicbop_zicboz_zicond1p0_zihintntl0p2_zihintpause_zawrs_zfa0p1_zfbfmin0p8_zfh_zca_zcb_zcd_zba_zbb_zbc_zbs_zvfbfmin0p8_zvfbfwma0p8_svinval_svpbmt_xtheadc_xtheadvdot -mabi=lp64d  -c -O2 --specs=nano.specs'.split())
#C_FLAGS.append('-std=c99')

# C and C++ generate define
CC_FLAGS = []
#CC_FLAGS.append('-Wall')


# ASM generate define
AS_FLAGS = []
#AS_FLAGS.append('-g')

# Link Config
LINK_FLAGS = "-T./lib/init/linker.lcf -nostartfiles  -mtune=c920 -march=rv64imafdcv_zicbom_zicbop_zicboz_zicond1p0_zihintntl0p2_zihintpause_zawrs_zfa0p1_zfbfmin0p8_zfh_zca_zcb_zcd_zba_zbb_zbc_zbs_zvfbfmin0p8_zvfbfwma0p8_svinval_svpbmt_xtheadc_xtheadvdot -mabi=lp64d"
LINK_FLAGS = LINK_FLAGS + ' -lc -lgcc -lm'
#LINK_FLAGS.append('-Wl,–gc-sections')


# lib path.
LIB_PATH = []
#LIB_PATH.append('lib')

# .lib, .a file
LIBS_FILES = []
#LIBS_FILES.append('test')

# spec ld flag. riscv spec.
SPEC_LD_FLAGS = []
if PLF == 'riscv':
    SPEC_LD_FLAGS.append('-Map')
    SPEC_LD_FLAGS.append(TARGET_WITHOUT_SUFFIX + '.map')
    SPEC_LD_FLAGS.append('-T' + 'src/map_ram.txt')


env = Environment()

###################################################################################
# Step0: toolchains setting.
if PLF == 'riscv':
    env['CC'] = CC
    env['AS'] = AS
    env['AR'] = AR
    env['CXX'] = CXX
    env['LINK'] = LINK

    env['OBJSUFFIX'] = '.o'
    env['LIBPREFIX'] = 'lib'
    env['LIBSUFFIX'] = '.a'
    env['PROGSUFFIX'] = '.elf'

###################################################################################
# Step1: C compile setting. use <print(env.Dump())> for details.
# 'CCCOM': '$CC -o $TARGET -c $CFLAGS $CCFLAGS $_CCCOMCOM $SOURCES'

# Step1.0: General options, like: optim/debug setting. $CFLAGS.
env.Append(CFLAGS=C_FLAGS)

# Step1.1: General options, other setting. $CCFLAGS.
env.Append(CCFLAGS=CC_FLAGS)

# Step1.2: -D, -I, setting. $_CCCOMCOM
# '_CCCOMCOM': '$CPPFLAGS $_CPPDEFFLAGS $_CPPINCFLAGS'
# StepX.2.0: CPPFLAGS setting. --- do nothing.
# StepX.2.1: -D setting. 
# 'CPPDEFPREFIX': '-D'
# '_CPPDEFFLAGS': '${_defines(CPPDEFPREFIX, CPPDEFINES, CPPDEFSUFFIX, __env__, '
#                 'TARGET, SOURCE)}',
env.Append(CPPDEFINES=CPP_DEFINES)
# Step1.2.2: -I setting. 
# 'INCPREFIX': '-I'
# '_CPPINCFLAGS': '${_concat(INCPREFIX, CPPPATH, INCSUFFIX, __env__, RDirs, '
#                 'TARGET, SOURCE, affect_signature=False)}',
env.Append(CPPPATH=CPP_PATH)

###################################################################################
# Step2: ASM compile setting. use <print(env.Dump())> for details.
# 'ASCOM': '$AS $ASFLAGS -o $TARGET $SOURCES'

# Step2.0: General options. $ASFLAGS.
env.Append(ASFLAGS=C_FLAGS)
env['ASCOM'] = env['ASPPCOM']

###################################################################################
# Step3: LINK setting. use <print(env.Dump())> for details.
# 'LINKCOM': '$LINK -o $TARGET $LINKFLAGS $__RPATH $SOURCES $_LIBDIRFLAGS '
#            '$_LIBFLAGS',

# Step3.0: General options. $LINKFLAGS.
env.Append(LINKFLAGS=LINK_FLAGS)

# Step3.1: Link path setting. $_LIBDIRFLAGS.
# '_LIBDIRFLAGS': '${_concat(LIBDIRPREFIX, LIBPATH, LIBDIRSUFFIX, __env__, '
#                 'RDirs, TARGET, SOURCE, affect_signature=False)}',
env.Append(LIBPATH=LIB_PATH)

# Step3.2: libs setting, like *.a, *.lib. $_LIBFLAGS.
#   '_LIBFLAGS': '${_stripixes(LIBLINKPREFIX, LIBS, LIBLINKSUFFIX, LIBPREFIXES, '
#                'LIBSUFFIXES, __env__)}',
env.Append(LIBS=LIBS_FILES)

# Step3.3: Add some spec params. must append at end.
#env.Append(_LIBFLAGS=SPEC_LD_FLAGS)


###################################################################################
# Step4: Compile Object files, use:
#        1. <$CCCOM>: For c code compile
#        2. <$ASCOM>: For asm code compile
current_dir = 'build/init'
lib_sources = find_sources("lib/init", ('.c', '.s', '.S'), 1)

# Create objects for each source file

objects = []
for src in lib_sources:
    obj_filename = os.path.basename(src).replace('.s', '.o')
    obj_path = os.path.join(current_dir, obj_filename)
    objects.append(env.Object(target=obj_path, source=src))


c_objs = env.Object(C_SRC_LIST)
as_objs = env.Object(AS_SRC_LIST)

###################################################################################
# Step5: Compile target <.elf>, use <$LINKCOM>.
target = env.Program(target = TARGET_WITHOUT_SUFFIX, source=[objects, c_objs, as_objs])
env['target'] = target

# Other compile target.
#env.Command(TARGET_WITHOUT_SUFFIX + '.bin', target, OBJCPY + ' -v -O binary $SOURCE $TARGET')
#env.Command(TARGET_WITHOUT_SUFFIX + '.lst', target, OBJDUMP + ' --source --all-headers --demangle --line-numbers --wide $SOURCE > $TARGET')
#env.Command(TARGET_WITHOUT_SUFFIX + '.size', target, SIZE + ' --format=berkeley $SOURCE')

SC_ROOT=os.getcwd()
CONVERT=f'{SC_ROOT}/lib/bin/Srec2vmem'
OBJDUMPFLAGS='-S -Mnumeric'
HEXFLAGS='-O srec'

inst_hex = OBJCPY + f' {HEXFLAGS} {os.path.join(SC_ROOT, str("$TARGET"))} -j .text* -j .rodata* -j .eh_frame* main_inst.hex;'
data_hex = OBJCPY + f' {HEXFLAGS} {os.path.join(SC_ROOT, str("$TARGET"))} -j .data* -j .bss -j .COMMON main_data.hex;'
test_hex = OBJCPY + f' {HEXFLAGS} {os.path.join(SC_ROOT, str("$TARGET"))} main.hex;'
inst_pat = CONVERT + f' main_inst.hex inst.pat;'
data_pat = CONVERT + f' main_data.hex data.pat;'
test_pat = CONVERT + f' main.hex case.pat;'

post_action = 'cd build;' + OBJDUMP + f' -D {OBJDUMPFLAGS} {os.path.join(SC_ROOT, str("$TARGET"))} > main.obj;'
post_action += inst_hex
post_action += data_hex
post_action += test_hex
post_action += inst_pat
post_action += data_pat
post_action += test_pat

env.AddPostAction(target, post_action)
# Dump() env params, if need.
#print(env.Dump())
