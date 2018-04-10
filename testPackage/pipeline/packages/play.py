"""This class just for to test package concept

:class:Play Test class concept
:meth:__init_ Just some methods

"""

class Play(object):
	"""inside :class:Play
	
	"""
	
	def __init__(self):
		""":class:Constructor Play for nothing
		
		"""
		
		pass
		
	def pre(self):
		
		"""docTest :meth:pre
		>>> for i in range(3):
		... 	print i
		0
		1
		2
		
		"""
		
		return ''
		
		
if __name__=="__main__":
	
	p=Play()
	p.pre()