class ProcessOutputThread(Thread): #OOPS
	def __init__(self, proc, conn):
		Thread.__init__(self)
		self.proc = proc
		self.conn = conn
		
	def run(self):
		while not self.proc.stdout.closed and not self.conn._closed:
			try:
				self.conn.sendall(self.proc.stdout.readline())
			except:
				pass
