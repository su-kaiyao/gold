mongoDB基本概念
===

### LAMP架构

- Linux
- Apache
- Mysql
- PHP

其中，M亦可以代表MongoDB

### mongoDB学习目标

1.了解mongoDB概念

- mongoDB
- mongo
- 索引
- 集合
- 复制集
- 分片
- 数据均衡

---

2.学会mongoDB搭建

- 搭建简单的单机服务
- 搭建具有冗余容错功能的复制集
- 搭建大规模数据集群
- 集群的自动部署

---

3.mongoDB的使用

- 最基本文档的读写更新删除
- 各种不同类型索引的创建与使用
- 复杂的聚合查询
- 对数据集合分片，在不同的分片间维持数据均衡
- 数据备份与恢复

---

4.简单运维

- 数据迁移
- 部署mongoDB集群
- 处理故障

### 与Mysql的比较

mongoDB无须预先定义任何表结构，开发敏捷，有完整的索引支持；但不支持事务操作

mongoDB具有方便的冗余与扩展性，复制集保证了数据的安全性以及其分片

### 与Redis的比较

皆为NoSql数据库，Redis不支持索引，是基于key的查询，但支持一点事务操作
