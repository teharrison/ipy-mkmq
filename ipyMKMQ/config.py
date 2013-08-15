import os

RETINA_URL     = 'http://raw.github.com/MG-RAST/Retina/master'
API_URL        = 'http://api.metagenomics.anl.gov/1'
CDMI_URL       = "http://kbase.us/services/cdmi_api"
NETWORKS_URL   = "http://140.221.92.76:7064/KBaseNetworksRPC/networks"
GENOPHENO_URL  = "http://140.221.84.160:7067"
ONTOLOGY_URL   = "http://140.221.84.160:7062"
EXPRESSION_URL = "http://140.221.84.160:7063"
try:
    KBASE_BIN  = os.path.join(os.environ['KB_TOP'], 'bin')
except:
    KBASE_BIN  = '/bin'
