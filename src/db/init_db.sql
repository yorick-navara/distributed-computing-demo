-- Local database definition.

DROP DATABASE IF EXISTS local_db;

CREATE DATABASE local_db;

USE local_db;

DROP TABLE IF EXISTS run_process;

CREATE TABLE run_process (
  id int(10) NOT NULL AUTO_INCREMENT,
  run_id varchar(36) NOT NULL,
  task_id varchar(36) NOT NULL,
  task_status varchar(16) NOT NULL DEFAULT '', -- values: 'created', 'started', 'completed', 'failed'
  worker_id varchar(16),
  PRIMARY KEY (id) -- TODO: set run_id and task_id as key
);
