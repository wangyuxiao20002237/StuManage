-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: stumanage1
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `stumanageapp_admin`
--

DROP TABLE IF EXISTS `stumanageapp_admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stumanageapp_admin` (
  `adminName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stumanageapp_admin`
--

LOCK TABLES `stumanageapp_admin` WRITE;
/*!40000 ALTER TABLE `stumanageapp_admin` DISABLE KEYS */;
INSERT INTO `stumanageapp_admin` VALUES ('admin','123456');
/*!40000 ALTER TABLE `stumanageapp_admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stumanageapp_course`
--

DROP TABLE IF EXISTS `stumanageapp_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stumanageapp_course` (
  `courseNo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `courseName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `courseGrade` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`courseNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stumanageapp_course`
--

LOCK TABLES `stumanageapp_course` WRITE;
/*!40000 ALTER TABLE `stumanageapp_course` DISABLE KEYS */;
INSERT INTO `stumanageapp_course` VALUES ('001','数据结构','2020'),('002','操作系统','2020'),('003','高等数学','2021'),('004','概率论','2022'),('005','马原','2020'),('006','毛概','2020'),('007','线性代数','2020'),('008','计算机组成原理','2019'),('009','软件测试','2021'),('010','编译原理','2021'),('011','机器学习','2019'),('012','计算机视觉','2019'),('013','模式识别','2020');
/*!40000 ALTER TABLE `stumanageapp_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stumanageapp_coursescore`
--

DROP TABLE IF EXISTS `stumanageapp_coursescore`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stumanageapp_coursescore` (
  `courseNo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `stuNo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `stuScore` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `courseGrade` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `id` varchar(100) DEFAULT NULL,
  `courseNo_id` varchar(100) DEFAULT NULL,
  `stuNo_id` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stumanageapp_coursescore`
--

LOCK TABLES `stumanageapp_coursescore` WRITE;
/*!40000 ALTER TABLE `stumanageapp_coursescore` DISABLE KEYS */;
INSERT INTO `stumanageapp_coursescore` VALUES ('001','20002237','90','2020',NULL,NULL,NULL),('001','20000002','80','2020',NULL,NULL,NULL),('002','20002237','','2020',NULL,NULL,NULL),('005','20002237','80','2020',NULL,NULL,NULL),('007','20002237','','2020',NULL,NULL,NULL),('006','20002237','','2020',NULL,NULL,NULL),('001','20000004','80','2020',NULL,NULL,NULL),('003','20000002','','2021',NULL,NULL,NULL),('008','20000003','','2019',NULL,NULL,NULL),('011','20000003','','2019',NULL,NULL,NULL),('012','20000003','','2019',NULL,NULL,NULL),('013','20002237','','2020',NULL,NULL,NULL),('013','20002241','','2020',NULL,NULL,NULL),('007','20002241','','2020',NULL,NULL,NULL),('005','20002241','','2020',NULL,NULL,NULL),('002','20002241','98','2020',NULL,NULL,NULL);
/*!40000 ALTER TABLE `stumanageapp_coursescore` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stumanageapp_student`
--

DROP TABLE IF EXISTS `stumanageapp_student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `stumanageapp_student` (
  `stuNo` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `stuName` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `stuAge` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `stuSex` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `stuGrade` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `password` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `status` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  PRIMARY KEY (`stuNo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stumanageapp_student`
--

LOCK TABLES `stumanageapp_student` WRITE;
/*!40000 ALTER TABLE `stumanageapp_student` DISABLE KEYS */;
INSERT INTO `stumanageapp_student` VALUES ('20000001','wwy','21','男','2020','20000001','0'),('20000002','www','21','男','2021','20000002','0'),('20000003','yre','21','女','2019','20000003','1'),('20000004','jkl','21','男','2020','20000004','1'),('20000005','yui','20','男','2020','20000005','1'),('20002237','wyx','22','男','2020','20002237','1'),('20002238','sdsf','22','男','2020','20002238','0'),('20002241','yuy','22','女','2020','20002241','1');
/*!40000 ALTER TABLE `stumanageapp_student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'stumanage1'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-12-08  9:11:25
