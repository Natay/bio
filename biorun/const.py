# Constants reused in the program

# JSON field names
DEFINITION = "definition"
DBLINK = "dblink"
LOCUS = "locus"
SEQID = "id"
ORIGIN = "ORIGIN"
FEATURES = "FEATURES"
FEATURE_COUNT = "feature_count"
ORIGIN_SIZE = "origin_len"

# Indentation character
INDENT = '  '

# Fields separator

SEP = ', '

CHUNK = 25000

COLOR_MAP = {'ends_during': '#449A5E', 'occurs_in': '#D537FD',
             'negatively_regulates': 'orange',
             'has_part': '#00FFFF',
             'is_a': '#000000',
             'part_of': "#727F2D",
             'positively_regulates': "#8D6B2E",
             'happens_during': "#6EB129",
             'regulates': "plum",
             'transcribed_to': "#98B7E4",
             'derives_from': "#AFCDB3",
             'contains': "#26A231",
             'member_of': "#1A851E",
             'transcribed_from': "#4B0201",
             'has_quality': "#35F081",
             'overlaps': "#C0441F",
             'variant_of': "#B47312",
             'non_functional_homolog_of': "#D149BE",
             'adjacent_to': "#E1D2B5",
             'guided_by': "#014B81",
             'has_origin': "#57F45B"
             }
# Alignment modes.
GLOBAL_ALIGN, LOCAL_ALIGN, SEMIGLOBAL_ALIGN, STRICT_GLOBAL_ALIGN = "global", "local", "semiglobal", "strictglobal"


# Command map
SUB_COMMANDS = [

    # Genome handler
    ("--genome", "biorun.models.fastarec"),
    ("-G", "biorun.models.fastarec"),

    # Fasta feature convertsion.
    ("--fasta", "biorun.models.fastarec"),
    ("-F", "biorun.models.fastarec"),

    # GFF conversion.
    ("--gff", "biorun.models.gffrec"),

    # Alignments.
    ("--align", "biorun.methods.align"),

    # Taxonomy browser.
    ("--taxon", "biorun.models.taxdb"),

    # Database links.
    ("--sra", "biorun.models.dblink"),

    # Ontology handlers.
    ("--define", "biorun.models.ontology"),

    # Default behaviors.
    ("-i", "biorun.models.fastarec"),
    ("--inter", "biorun.models.fastarec"),

]

SKIP_GFF_ATTR = {"id", "parent_id", "name", "type", "start", "end", "location", "translation", "strand", "operator"}

# Guess accession numbers that are proteins based on start letters
# https: // www.ncbi.nlm.nih.gov / Sequin / acc.html

#
# Remaps types from GenBank to Sequence Ontology when converting to GFF files
#

NCBI_PROTEIN_CODES = {"AP", "NP", "YP", "XP", "WP", "AK"}

NCBI_NUCLEOTIDE_CODES = {"NM", "NX", "YP", "XP", "WP", "AK"}

BUCKET_NAME = "biostore-bucket-001"

# Types with hierachies
MULTIPART_TYPES = {"mRNA", "CDS", "ncRNA", "tRNA"}

SEQUENCE_ONTOLOGY = {
    "source": "region",
    "5'UTR": "five_prime_UTR",
    "3'UTR": "three_prime_UTR",
    "mat_peptide": "mature_protein_region",
}

# Feature types where the name of the feature is predetermined.
NAME_FROM_TYPE = {
    "five_prime_UTR": "five_prime_UTR",
    "three_prime_UTR": "three_prime_UTR",
    "stem_loop": "stem_loop",
}

# Associates a color to a feature type.
COLOR_FOR_TYPE = {
    "five_prime_UTR": "#cc0e74",
    "three_prime_UTR": "#cc0e74",
    "stem_loop": "#fa7f72",
    "mature_protein_region": "#CBAEBB",
    "region": "#CECECE",
    "mRNA": "#799351",
    "gene": "#cb7a77",
    "transcript": "#79a3b1",
    "tRNA": "#a685e2",
    "ncRNA": "#fca3cc",
    "mobile_element": "#efd9d1",
    "mRNA_region":"#7a77cb",
}
#
# The GFF attributes generated for a source type.
#
SOURCE_ATTRIBUTES = [
    "mol_type", "isolate", "db_xref", "organism", "country", "collection_date"
]

# GFF attributes filled for each feature other than "source"
GFF_ATTRIBUTES = [
    "gene", "protein_id", "product", "db_xref", "function",
]

# Recognized types.
GENBANK, FASTA, GFF, BED, SAM, BAM = "genbank", "fasta", "gff", "bed", "sam", "bam"

# Connect an extension to types.
TYPE_BY_EXTENSION = {
    "gb": GENBANK,
    "gbk": GENBANK,
    "genbank": GENBANK,
    "fa": FASTA,
    "fasta": FASTA,
    "bed": BED,
    "gff": GFF,
    "sam": SAM,
    "bam": BAM,
}
