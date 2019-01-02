create table bacs
(
  BACS_sys_id      int(64) auto_increment,
  BACS_code        varchar(20)  null,
  est_name         varchar(200) null,
  case_num         varchar(20)  null,
  epricing_num     varchar(20)  null,
  status           varchar(40)  null,
  applicant        varchar(40)  null,
  team             varchar(40)  null,
  apply_date       varchar(20)  null,
  epricing_status  varchar(40)  null,
  offer_price      float        null,
  total_sr_price   float        null,
  discount_rate    float        null,
  last_update_date varchar(20)  null,
  constraint BACS_BACS_sys_id_uindex
  unique (BACS_sys_id)
);

alter table bacs
  add primary key (BACS_sys_id);

create table bacs_approval_process
(
  BACS_approval_process_id int(64) auto_increment,
  BACS_code                varchar(20)  null,
  approval_action          varchar(20)  null,
  aproval_remark           varchar(500) null,
  action_by                varchar(100) null,
  status                   varchar(20)  null,
  constraint bacs_approval_process_BACS_approval_process_id_uindex
  unique (BACS_approval_process_id)
);

alter table bacs_approval_process
  add primary key (BACS_approval_process_id);

create table bacs_item
(
  bacs_item_sys_id int(64) auto_increment,
  bacs_code        varchar(20)  null,
  item_num         varchar(40)  null,
  item_name        varchar(200) null,
  qty              int          null,
  unit_price       float        null,
  total            float        null,
  rev_allocate     float        null,
  constraint bacs_item_bacs_item_sys_id_uindex
  unique (bacs_item_sys_id)
);

alter table bacs_item
  add primary key (bacs_item_sys_id);


