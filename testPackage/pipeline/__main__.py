import sys
from .packages import *

def _lunch():
	print dir(Z),'hello'
	print help(Z)
	print sys.path
	
if __name__=="__main__":
	_lunch()