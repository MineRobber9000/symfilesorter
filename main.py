import symfile,argparse
parser = argparse.ArgumentParser(description="Sorts a symfile.")
parser.add_argument("symfile",help="Symfile to sort.")
args = parser.parse_args()
sym = symfile.SymFile(args.symfile)
with open(args.symfile,"w") as f:
	sym.output(f)
