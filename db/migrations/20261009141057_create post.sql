-- migrate:up

CREATE TABLE post (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT now()
);

-- migrate:down

DROP TABLE post;
