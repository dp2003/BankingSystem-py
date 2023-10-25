-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jul 24, 2021 at 05:36 PM
-- Server version: 10.4.19-MariaDB
-- PHP Version: 7.3.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `bank`
--

-- --------------------------------------------------------

--
-- Table structure for table `customer`
--

CREATE TABLE `customer` (
  `id` int(11) NOT NULL,
  `FullName` varchar(50) NOT NULL,
  `Age` int(5) NOT NULL,
  `Address` varchar(100) NOT NULL,
  `Mobile` varchar(50) NOT NULL,
  `Occupation` varchar(20) NOT NULL,
  `AccountNo` int(20) NOT NULL,
  `AccountType` varchar(10) NOT NULL,
  `Balance` float NOT NULL,
  `CustUser` varchar(11) NOT NULL,
  `CustPass` varchar(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `customer`
--

INSERT INTO `customer` (`id`, `FullName`, `Age`, `Address`, `Mobile`, `Occupation`, `AccountNo`, `AccountType`, `Balance`, `CustUser`, `CustPass`) VALUES
(1, 'Joe Woodson', 50, 'C/19, Sunshine Appartment, Andheri(West)', '9856378292', 'Government Servent', 1001, 'Savings', 200000, 'abc', '123'),
(2, 'Serena Smith', 31, 'A/5, Rose Villa, Goregoan(West)', '9846502711', 'Bank Executive', 1002, 'Savings', 3000000, 'xyz', '345'),
(3, 'Lily Smith', 50, 'B/12, Sea View Appartments, Bandra(East)', '9853621937', 'Employee', 1003, 'Savings', 350000, 'pqr', '987'),
(4, 'Sarah Jade', 35, 'C/16,Diwan Mension, Bandra(East)', '8794536729', 'Bank Executive', 1004, 'Savings', 5000000, 'lmn', '567'),
(5, 'Charls Winston', 33, 'D/13,Amazon,Vile Parle(West)', '8790345279', 'Businessmen', 1005, 'Current', 50000000, 'def', '789');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `customer`
--
ALTER TABLE `customer`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `customer`
--
ALTER TABLE `customer`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
