-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 18, 2019 at 09:48 AM
-- Server version: 10.1.35-MariaDB
-- PHP Version: 7.2.9

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `event`
--

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `depid` int(11) NOT NULL,
  `depname` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`depid`, `depname`) VALUES
(1, 'cse'),
(2, 'ece'),
(3, 'chemical engg'),
(4, 'mech'),
(5, 'mbbs'),
(6, 'bca'),
(7, 'bcom'),
(8, 'bba');

-- --------------------------------------------------------

--
-- Table structure for table `events`
--

CREATE TABLE `events` (
  `eventid` int(11) NOT NULL,
  `eventname` varchar(50) NOT NULL,
  `eventdepartment` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `events`
--

INSERT INTO `events` (`eventid`, `eventname`, `eventdepartment`) VALUES
(1, 'singing', 1),
(2, 'painting', 2),
(3, 'dancing', 6),
(4, 'web development', 1),
(5, 'on the spot poster making', 7),
(8, 'writing', NULL),
(9, 'math quiz', NULL),
(11, 'future robot', NULL),
(13, 'art', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `registration`
--

CREATE TABLE `registration` (
  `regid` int(11) NOT NULL,
  `regstudent` int(11) DEFAULT NULL,
  `studentdepartment` int(11) DEFAULT NULL,
  `eventname` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `registration`
--

INSERT INTO `registration` (`regid`, `regstudent`, `studentdepartment`, `eventname`) VALUES
(7, 4, 2, 4),
(8, 3, NULL, 2),
(16, 12, NULL, 1),
(22, 14, NULL, 1),
(35, 16, NULL, 8),
(36, 18, NULL, 11),
(38, 1, NULL, 1),
(39, 1, NULL, 1),
(40, 1, NULL, 8),
(41, 19, NULL, 1),
(42, 19, NULL, 1),
(43, 20, NULL, 2);

-- --------------------------------------------------------

--
-- Table structure for table `students`
--

CREATE TABLE `students` (
  `stuid` int(11) NOT NULL,
  `stuname` varchar(20) NOT NULL,
  `fathername` varchar(30) NOT NULL,
  `email` varchar(50) NOT NULL,
  `studep` int(11) DEFAULT NULL,
  `PASSWORD` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `students`
--

INSERT INTO `students` (`stuid`, `stuname`, `fathername`, `email`, `studep`, `PASSWORD`) VALUES
(1, 'narayan jha', 'ram lal jha', 'naraynjha@gmail.com', 1, 'welcome12'),
(2, 'amit kumar', 'akhilesh kumar', 'ak234@gmail.com', 1, 'airbag12'),
(3, 'purnima sinha', 'akhilesh kumar', 'purnimasinha123@gmail.com', 2, 'puru123'),
(4, 'anjali jha', 'ram lal jha', 'anjali234@gmial.com', 6, 'doll123'),
(5, 'arnav', 'manoj sinha', 'ak2345@gmail.com', 3, 'sys123'),
(8, 'anshu', 'akhilesh', 'anshu1232@gmail.com', 6, 'iuhuihuiu'),
(9, 'monu', 'papa', 'anshu1232@gmail.com', 8, 'welcome'),
(12, 'jasmeet kaur', 'surjeet singh', 'jasmeet.212.kaur@gmail.com', 2, 'jasmeet'),
(14, 'pur', 'papa', 'pap@gmail.com', 2, 'welcome12'),
(15, 'monu', 'papa gg', 'kaka@monu.com', 1, '123456789'),
(16, 'purnima', 'papaaa', 'khushboo@gmail.com', 2, 'indiacan'),
(17, 'manisha', 'papaaa', 'khushboo@gmail.com', 2, 'indiacan'),
(18, 'anshu', 'akhilesh', 'aru@gmail', 3, 'arushi'),
(19, 'Ram Krishan', 'Ddday', 'ram@gmail.com', 1, '1234567'),
(20, 'aishwarya', 'papa', 'aish@gmail.com', 1, 'welcome');

-- --------------------------------------------------------

--
-- Table structure for table `tbadmin`
--

CREATE TABLE `tbadmin` (
  `admid` int(11) NOT NULL,
  `admuserid` varchar(50) NOT NULL,
  `admpassword` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `tbadmin`
--

INSERT INTO `tbadmin` (`admid`, `admuserid`, `admpassword`) VALUES
(10, 'purnimasinha123@gmail.com', 'welcome'),
(11, 'narayanjha@gmail.com', 'machine12'),
(12, 'amitkumar91@gmail.com', 'pagal12'),
(13, 'ram123@gmail.com', '123pgas'),
(14, 'ak717321@gmail.com', 'amitkumar'),
(15, 'admin', 'admin'),
(17, 'amitkumar916@gmail.com', 'adminn');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`depid`);

--
-- Indexes for table `events`
--
ALTER TABLE `events`
  ADD PRIMARY KEY (`eventid`),
  ADD KEY `eventdepartment` (`eventdepartment`);

--
-- Indexes for table `registration`
--
ALTER TABLE `registration`
  ADD PRIMARY KEY (`regid`),
  ADD KEY `regstudent` (`regstudent`),
  ADD KEY `studentdepartment` (`studentdepartment`),
  ADD KEY `eventname` (`eventname`);

--
-- Indexes for table `students`
--
ALTER TABLE `students`
  ADD PRIMARY KEY (`stuid`),
  ADD KEY `studep` (`studep`);

--
-- Indexes for table `tbadmin`
--
ALTER TABLE `tbadmin`
  ADD PRIMARY KEY (`admid`),
  ADD UNIQUE KEY `admuserid` (`admuserid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `department`
--
ALTER TABLE `department`
  MODIFY `depid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=9;

--
-- AUTO_INCREMENT for table `events`
--
ALTER TABLE `events`
  MODIFY `eventid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT for table `registration`
--
ALTER TABLE `registration`
  MODIFY `regid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `students`
--
ALTER TABLE `students`
  MODIFY `stuid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `tbadmin`
--
ALTER TABLE `tbadmin`
  MODIFY `admid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `events`
--
ALTER TABLE `events`
  ADD CONSTRAINT `events_ibfk_1` FOREIGN KEY (`eventdepartment`) REFERENCES `department` (`depid`);

--
-- Constraints for table `registration`
--
ALTER TABLE `registration`
  ADD CONSTRAINT `registration_ibfk_1` FOREIGN KEY (`regstudent`) REFERENCES `students` (`stuid`),
  ADD CONSTRAINT `registration_ibfk_2` FOREIGN KEY (`studentdepartment`) REFERENCES `department` (`depid`),
  ADD CONSTRAINT `registration_ibfk_3` FOREIGN KEY (`eventname`) REFERENCES `events` (`eventid`);

--
-- Constraints for table `students`
--
ALTER TABLE `students`
  ADD CONSTRAINT `students_ibfk_1` FOREIGN KEY (`studep`) REFERENCES `department` (`depid`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
