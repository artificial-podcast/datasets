

.PHONY: all
all: sync_generated

.PHONY: sync_generated
sync_generated:
	cd texts/generated && gsutil -m rsync -x ".*\.tar.gz$\" -i -r gs://artificial-podcast/jobs .

.PHONY: sync_legacy
sync_legacy:
	cd texts/generated/legacy && gsutil -m rsync -x ".*\.tar.gz$\" -i -r gs://artificial-podcast/generated .
