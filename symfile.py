from collections import OrderedDict

class SymFile:
	def __init__(self,filename):
		self.rom = OrderedDict()
		self.wram = []
		self.sram = []
		self.vram = []
		self.misc = []
		with open(filename) as f:
			lines = [l.strip() for l in f]
			for line in lines:
				if not line:
					continue
				if line.startswith(";"):
					continue
				highnibble=line[3]
				bank = int(line[0:2],16)
				if highnibble in ("0","1","2","3","4","5","6","7"):
					if bank in self.rom:
						self.rom[bank].append(line)
					else:
						self.rom[bank]=[line]
				elif highnibble in ("8","9"):
					self.vram.append(line)
				elif highnibble in ("A","B"):
					self.sram.append(line)
				elif highnibble in ("C","D") or line[3:7]=="E000": # edge case: XX:E000 is a valid WRAM label
					self.wram.append(line)
				else:
					self.misc.append(line)
		for k in self.rom:
			self.rom[k].sort()
		self.wram.sort()
		self.vram.sort()
		self.sram.sort()
		self.misc.sort()

	def output(self,f):
		f.write("; ROM\n")
		for bank in self.rom.keys():
			f.write("\n".join(self.rom[bank])+"\n")
		if self.vram:
			f.write("; VRAM\n")
			f.write("\n".join(self.vram)+"\n")
		if self.sram:
			f.write("; SRAM\n")
			f.write("\n".join(self.sram)+"\n")
		if self.wram:
			f.write("; WRAM\n")
			f.write("\n".join(self.wram)+"\n")
		if self.misc:
			f.write("; Other addresses (HRAM)")
			f.write("\n".join(self.misc))
