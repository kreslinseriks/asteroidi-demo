-- Migracija pievieno jaunu kolonnu ar nosaukumu "materiaals"

ALTER TABLE ast_daily
ADD COLUMN material VARCHAR(255) DEFAULT 'Unknown';