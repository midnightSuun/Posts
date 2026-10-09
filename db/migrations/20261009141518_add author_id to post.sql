-- migrate:up

ALTER TABLE post
    ADD COLUMN author_id INTEGER NOT NULL,
    ADD CONSTRAINT post_author_id_fkey FOREIGN KEY (author_id) REFERENCES "user" (id);

-- migrate:down

ALTER TABLE post
    DROP COLUMN author_id;
