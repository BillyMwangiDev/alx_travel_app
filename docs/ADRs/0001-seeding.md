# ADR 0001: Database Seeding Approach

## Context
We need deterministic, lightweight seed data to support frontend development and QA. Avoid extra dependencies like Faker in core requirements.

## Decision
- Implement a `seed` management command that creates N listings with M bookings and reviews.
- Use basic Python stdlib for dates, deterministic values for reproducibility.
- Provide `--flush` option to clear existing seeded data.

## Consequences
- No randomization means consistent test and demo data.
- Easy to extend with optional Faker later if required.


