# This is an autogenerated file. It serves as a starting point
# for a more percise manual annotation of this module.
# Feel free to edit the source below, but remove this header when you do.

MAGIC = Undefined(int)
MAXREPEAT = Undefined(long)
CODESIZE = Undefined(int)
copyright = Undefined(str)

def getlower(a: int, b: int) -> int: pass

def compile(a, b: int, c, *args, **kwargs) -> SRE_Pattern:
    raise OverflowError()

def getcodesize() -> int: pass


class SRE_Match(object):
    def group(*args, **kwargs) -> tuple: pass
    def start(*args, **kwargs) -> int:
        raise IndexError()
    def end(*args, **kwargs) -> int:
        raise IndexError()
    def span(*args, **kwargs) -> tuple:
        raise IndexError()
    def groups(*args, **kwargs) -> tuple: pass
    def groupdict(*args, **kwargs) -> dict: pass
    def expand(*args, **kwargs) -> object: pass
    def __copy__() -> object:
        raise TypeError()
    def __deepcopy__(*args, **kwargs) -> object:
        raise TypeError()

class SRE_Pattern(object):
    def match(pattern, *args, **kwargs) -> object: pass
    def search(pattern, *args, **kwargs) -> object: pass
    def sub(repl, string, *args, **kwargs) -> tuple: pass
    def subn(repl, string, *args, **kwargs) -> tuple: pass
    def split(source, *args, **kwargs) -> List[NoneType]: pass
    def findall(source, *args, **kwargs) -> List[tuple]: pass
    def finditer(*args, **kwargs) -> callable_iterator: pass
    def scanner(a, *args, **kwargs) -> SRE_Scanner: pass
    def __copy__() -> object:
        raise TypeError()
    def __deepcopy__(*args, **kwargs) -> object:
        raise TypeError()

class SRE_Scanner(object):
    def match() -> object: pass
    def search() -> object: pass