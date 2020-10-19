import os, csv
from biorun import __main__ as bio
import plac
from biorun.align import pairwise

# The path to the current file.
__CURR_DIR = os.path.dirname(__file__)

__DATADIR = os.path.join(__CURR_DIR, "data")

def read(fname, datadir=__DATADIR):
    path = os.path.join(datadir, fname) if datadir else fname
    text = open(path).read()
    return text

def run(cmd, capsys, out=None):
    """
    Runs a command and returns its out.
    """

    # Take the parameters only.
    params = cmd.split()[1:]

    # Run the command and assert its state.
    assert plac.call(bio.run, params) == None

    # Read the standard out
    stream = capsys.readouterr()
    result = stream.out

    if out:
        # Print only a subsection of the file
        if result != out:
            lines = result.splitlines()[:5]
            text = "\n".join(lines)
            print(text)
            assert False

    return result

def test_fetch(capsys):
    cmd = "bio fetch NC_045512"
    run(cmd, capsys=capsys)

def test_list(capsys):
    cmd = "bio data"
    run(cmd, capsys=capsys)

def test_view(capsys):
    cmd = "bio view NC_045512"
    out = read("NC_045512.json")
    run(cmd, capsys=capsys, out=out)

def test_view_match(capsys):
    cmd = "bio view NC_045512 --match ORF1ab --type gene "
    out = read("parts/match.json")
    run(cmd, capsys=capsys, out=out)

def test_view_list(capsys):
    cmd = "bio data"
    run(cmd, capsys=capsys)

def test_view_fasta(capsys):
    cmd = "bio view NC_045512 --fasta"
    out = read("NC_045512.fa")
    run(cmd, capsys=capsys, out=out)

def test_view_fasta_start(capsys):
    cmd = "bio view NC_045512 --fasta --id foo --start 10 --end 20"
    out = read("parts/fasta-start.fa")
    run(cmd, capsys=capsys, out=out)

def test_protein_end(capsys):
    cmd = "bio view NC_045512 --protein --start -10"
    out = read("parts/protein-end.fa")
    run(cmd, capsys=capsys, out=out)

def test_view_fasta_type(capsys):
    cmd = "bio view NC_045512 --fasta --type CDS"
    out = read("parts/CDS.fa")
    run(cmd, capsys=capsys, out=out)

def test_view_fasta_type_start(capsys):
    cmd = "bio view NC_045512 --fasta --type gene --end 10"
    out = read("parts/gene-start.fa")
    run(cmd, capsys=capsys, out=out)

def test_view_gff1(capsys):
    cmd = "bio view NC_045512 --gff"
    out = read("NC_045512.gff")
    run(cmd, capsys=capsys, out=out)

def test_view_gff_name(capsys):
    cmd = "bio view NC_045512 --gff --gene S"
    out = read("parts/gene.gff")
    run(cmd, capsys=capsys, out=out)

def test_view_gff_start(capsys):
    cmd = "bio view NC_045512 --gff  --start 10000 --end 20000"
    out = read("parts/overlap.gff")
    run(cmd, capsys=capsys, out=out)

def test_view_gff_type(capsys):
    cmd = "bio view NC_045512 --gff  --type CDS"
    out = read("parts/type.gff")
    run(cmd, capsys=capsys, out=out)

def main():
    pass

if __name__ == '__main__':
    main()
