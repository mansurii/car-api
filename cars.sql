-- Create the "cars" table
create table cars (
  -- auto-incrementing unique ID for each car
  id bigint generated always as identity primary key,
  -- car manufacturer, required
  brand text not null,
  -- car model name, required
  model text not null,
  -- manufacturing year, required
  year int not null,
  -- timestamp of when the row was created, auto-filled
  created_at timestamptz default now()
);

-- Enable Row Level Security (RLS) on the "cars" table
-- This blocks all access by default until policies are added
alter table cars enable row level security;

-- Allow anyone (unauthenticated/anon users) to read (SELECT) rows from "cars"
create policy "Allow public read access"
on cars
for select
to anon
using (true);