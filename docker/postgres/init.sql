-- BRIDGE Database Initialization
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_trgm";
ALTER DATABASE bridge_lewis_db SET timezone TO 'America/La_Paz';

-- Create schemas for organization
CREATE SCHEMA IF NOT EXISTS bridge_auth;
CREATE SCHEMA IF NOT EXISTS bridge_business;
CREATE SCHEMA IF NOT EXISTS bridge_audit;

COMMENT ON DATABASE bridge_lewis_db IS 'BRIDGE SaaS Database - Lewis Configuration';
