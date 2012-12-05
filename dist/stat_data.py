# Auto-generate statistics #defines, with allocation, clear and print functions.
#
# The XXX_stats dictionaries are a set of objects consisting of comma-separated
# configuration key words and a text description.  The configuration key words
# are:
#	perm	-- Field is not cleared by the stat clear function.

from operator import attrgetter

class Stat:
	def __init__(self, name, desc, **flags):
		self.name = name
		self.desc = desc
		self.flags = flags

	def __cmp__(self, other):
		return cmp(self.name, other.name)

##########################################
# CONNECTION statistics
##########################################
connection_stats = [
	##########################################
	# System statistics
	##########################################
	Stat('cond_wait', 'pthread mutex condition wait calls'),
	Stat('memory_allocation', 'total heap memory allocations'),
	Stat('memory_free', 'total heap memory frees'),
	Stat('read_io', 'total read I/Os'),
	Stat('rwlock_read', 'pthread mutex shared lock read-lock calls'),
	Stat('rwlock_write', 'pthread mutex shared lock write-lock calls'),
	Stat('write_io', 'total write I/Os'),

	##########################################
	# Btree statistics
	##########################################
	Stat('btree_file_open', 'btree (including LSM) files currently open'),

	##########################################
	# Block manager statistics
	##########################################
	Stat('block_byte_read', 'bytes read by the block manager'),
	Stat('block_byte_write', 'bytes written by the block manager'),
	Stat('block_read', 'blocks read by the block manager'),
	Stat('block_write', 'blocks written by the block manager'),

	##########################################
	# Cache and eviction statistics
	##########################################
	Stat('cache_bytes_dirty', 'cache: tracked dirty bytes in the cache'),
	Stat('cache_bytes_inuse',
	    'cache: bytes currently in the cache', perm=1),
	Stat('cache_bytes_max', 'cache: maximum bytes configured', perm=1),
	Stat('cache_bytes_read', 'cache: bytes read into cache'),
	Stat('cache_bytes_write', 'cache: bytes written from cache'),
	Stat('cache_eviction_clean', 'cache: unmodified pages evicted'),
	Stat('cache_eviction_dirty', 'cache: modified pages evicted'),
	Stat('cache_eviction_fail',
	    'cache: pages selected for eviction unable to be evicted'),
	Stat('cache_eviction_hazard',
	    'cache: eviction unable to acquire hazard reference'),
	Stat('cache_eviction_internal', 'cache: internal pages evicted'),
	Stat('cache_eviction_slow',
	    'cache: eviction server unable to reach eviction goal'),
	Stat('cache_pages_dirty', 'cache: tracked dirty pages in the cache'),
	Stat('cache_pages_inuse',
	    'cache: pages currently held in the cache', perm=1),
	Stat('cache_read', 'cache: pages read into cache'),
	Stat('cache_write', 'cache: pages written from cache'),

	##########################################
	# Transaction statistics
	##########################################
	Stat('txn_ancient', 'ancient transactions'),
	Stat('txn_begin', 'transactions'),
	Stat('txn_checkpoint', 'transaction checkpoints'),
	Stat('txn_commit', 'transactions committed'),
	Stat('txn_fail_cache', 'transaction failures due to cache overflow'),
	Stat('txn_rollback', 'transactions rolled-back'),
]

connection_stats = sorted(connection_stats, key=attrgetter('name'))

##########################################
# Data source statistics
##########################################
dsrc_stats = [
	##########################################
	# Operations
	##########################################
	Stat('cursor_insert', 'cursor-inserts'),
	Stat('cursor_next', 'cursor next'),
	Stat('cursor_prev', 'cursor prev'),
	Stat('cursor_remove', 'cursor remove'),
	Stat('cursor_reset', 'cursor reset'),
	Stat('cursor_search', 'cursor search'),
	Stat('cursor_search_near', 'cursor search near'),
	Stat('cursor_update', 'cursor update'),

	##########################################
	# Btree statistics
	##########################################
	Stat('btree_column_deleted',
	    'column-store variable-size deleted values'),
	Stat('btree_column_fix', 'column-store fixed-size leaf pages'),
	Stat('btree_column_internal', 'column-store internal pages'),
	Stat('btree_column_variable', 'column-store variable-size leaf pages'),
	Stat('btree_compact_rewrite', 'tree pages rewritten by compaction'),
	Stat('btree_entries', 'total key/value pairs'),
	Stat('btree_entries_bulk_loaded', 'total bulk-loaded key/value pairs'),
	Stat('btree_fixed_len', 'fixed-record size'),
	Stat('btree_maxintlitem', 'maximum internal page item size'),
	Stat('btree_maxintlpage', 'maximum internal page size'),
	Stat('btree_maxleafitem', 'maximum leaf page item size'),
	Stat('btree_maxleafpage', 'maximum leaf page size'),
	Stat('btree_overflow', 'overflow pages'),
	Stat('btree_row_internal', 'row-store internal pages'),
	Stat('btree_row_leaf', 'row-store leaf pages'),

	##########################################
	# LSM statistics
	##########################################
	Stat('bloom_count', 'bloom filters in the LSM tree'),
	Stat('bloom_false_positive', 'bloom filter false positives'),
	Stat('bloom_hit', 'bloom filter hits'),
	Stat('bloom_miss', 'bloom filter misses'),
	Stat('bloom_page_evict', 'bloom filter pages evicted from cache'),
	Stat('bloom_page_read', 'bloom filter pages read into cache'),
	Stat('bloom_size', 'total size of bloom filters'),
	Stat('lsm_chunk_count', 'chunks in the LSM tree'),
	Stat('lsm_generation_max', 'highest merge generation in the LSM tree'),
	Stat('lsm_lookup_no_bloom',
	    'queries that could have benefited ' +
	    'from a Bloom filter that did not exist'),

	##########################################
	# Block manager statistics
	##########################################
	Stat('block_alloc', 'blocks allocated'),
	Stat('block_allocsize', 'block manager file allocation unit size'),
	Stat('block_checkpoint_size', 'checkpoint size'),
	Stat('block_extension', 'block allocations requiring file extension'),
	Stat('block_free', 'blocks freed'),
	Stat('block_magic', 'file magic number'),
	Stat('block_major', 'file major version number'),
	Stat('block_minor', 'minor version number'),
	Stat('block_size', 'block manager size'),

	##########################################
	# Cache and eviction statistics
	##########################################
	Stat('cache_bytes_changed',
	    'approximate measure of bytes changed: counts key and value ' +
	    'bytes inserted with cursor.insert, value bytes updated with ' +
	    'cursor.update and key bytes removed using cursor.remove'),
	Stat('cache_bytes_read', 'bytes read into cache'),
	Stat('cache_bytes_write', 'bytes written from cache'),
	Stat('cache_eviction_clean', 'unmodified pages evicted'),
	Stat('cache_eviction_dirty', 'modified pages evicted'),
	Stat('cache_eviction_fail',
	    'data source pages selected for eviction unable to be evicted'),
	Stat('cache_eviction_hazard',
	    'eviction unable to acquire hazard reference'),
	Stat('cache_eviction_internal', 'internal pages evicted'),
	Stat('cache_overflow_value', 'overflow values cached in memory'),
	Stat('cache_read', 'pages read into cache'),
	Stat('cache_read_overflow', 'overflow pages read into cache'),
	Stat('cache_write', 'pages written from cache'),

	##########################################
	# Reconciliation statistics
	##########################################
	Stat('rec_dictionary', 'reconciliation dictionary matches'),
	Stat('rec_ovfl_key', 'reconciliation overflow keys written'),
	Stat('rec_ovfl_value', 'reconciliation overflow values written'),
	Stat('rec_page_delete', 'reconciliation pages deleted'),
	Stat('rec_page_merge', 'reconciliation pages merged'),
	Stat('rec_split_intl', 'reconciliation internal pages split'),
	Stat('rec_split_leaf', 'reconciliation leaf pages split'),
	Stat('rec_written', 'reconciliation pages written'),

	##########################################
	# Transaction statistics
	##########################################
	Stat('txn_update_conflict', 'update conflicts'),
	Stat('txn_write_conflict', 'write generation conflicts'),
]

dsrc_stats = sorted(dsrc_stats, key=attrgetter('name'))
