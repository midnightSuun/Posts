-- migrate:up

ALTER TABLE users RENAME TO "user";
ALTER TABLE "user" RENAME CONSTRAINT users_pkey TO user_pkey;
ALTER TABLE "user" RENAME CONSTRAINT users_email_key TO user_email_key;
ALTER SEQUENCE users_id_seq RENAME TO user_id_seq;

-- migrate:down

ALTER SEQUENCE user_id_seq RENAME TO users_id_seq;
ALTER TABLE "user" RENAME CONSTRAINT user_email_key TO users_email_key;
ALTER TABLE "user" RENAME CONSTRAINT user_pkey TO users_pkey;
ALTER TABLE "user" RENAME TO users;
