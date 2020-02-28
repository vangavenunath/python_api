-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: itccnet_venu
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `v_user_log`
--

DROP TABLE IF EXISTS `v_user_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `v_user_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `create_date` date NOT NULL,
  `start_time` time DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `last_updated` datetime NOT NULL,
  `comment` text,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=24 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `v_user_log`
--

LOCK TABLES `v_user_log` WRITE;
/*!40000 ALTER TABLE `v_user_log` DISABLE KEYS */;
INSERT INTO `v_user_log` VALUES (23,'user111','2020-02-20','09:00:00','17:00:00','2020-02-20 16:56:14','<p><strong>test22223</strong></p>'),(18,'user111','2020-02-17','09:00:00','17:00:00','2020-02-19 16:40:27','<p>test2</p>'),(19,'user111','2020-02-14','09:00:00','17:00:00','2020-02-19 16:40:35','<p>test3</p>'),(20,'user1','2020-02-18','09:00:00','17:00:00','2020-02-19 16:42:06','<p><strong>asdfasdf</strong></p><figure class=\"media\"><oembed url=\"https://www.youtube.com/watch?v=6kZ2i74HVA8\"></oembed></figure>'),(17,'user111','2020-02-18','09:00:00','17:00:00','2020-02-19 16:40:20','<p>test1</p>'),(22,'user111','2020-02-19','09:00:00','17:00:00','2020-02-20 16:55:55','<p>test22223</p>'),(14,'user1','2020-02-16','09:00:00','17:00:00','2020-02-19 16:10:44','<p>test1</p>'),(21,'user1','2020-02-19','09:00:00','17:00:00','2020-02-20 16:54:42','<p>test22</p>'),(16,'user1','2020-02-17','09:00:00','17:00:00','2020-02-19 16:20:01','');
/*!40000 ALTER TABLE `v_user_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `v_user_login`
--

DROP TABLE IF EXISTS `v_user_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `v_user_login` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `last_updated` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `v_user_login`
--

LOCK TABLES `v_user_login` WRITE;
/*!40000 ALTER TABLE `v_user_login` DISABLE KEYS */;
INSERT INTO `v_user_login` VALUES (1,'admin','admin','2020-02-14 10:00:00'),(12,'venu551','pass551','2020-02-18 12:13:35'),(7,'user1','pass1','2020-02-18 09:43:37'),(8,'user111','pass111','2020-02-18 10:36:08'),(13,'user2','pass2','2020-02-20 16:50:45');
/*!40000 ALTER TABLE `v_user_login` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-20 17:05:28



CREATE TABLE v_user_leaves (
	id INT  NOT NULL PRIMARY KEY AUTO_INCREMENT,
	username varchar(50),
    leave_date date,
    leave_status varchar(20),
    last_updated datetime NOT NULL
);


INSERT INTO v_user_leaves
SELECT 1,'user1','20200227','pending',now()
commit;

select username, leave_date, last_updated from v_user_leaves where leave_status = 'pending';

CREATE TABLE v_user_leaves (
	id INT  NOT NULL PRIMARY KEY AUTO_INCREMENT,
	username varchar(50),
    leave_date date,
    leave_status varchar(20),
    last_updated datetime NOT NULL
);

UPDATE v_user_leaves SET leave_status = 'pending' WHERE leave_status != 'pending' AND id != 0;
commit;
