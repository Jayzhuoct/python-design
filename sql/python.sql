SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for phones
-- ----------------------------
DROP TABLE IF EXISTS `phones`;
CREATE TABLE `phones` (
  `id` int NOT NULL AUTO_INCREMENT,
  `brand` varchar(50) NOT NULL,
  `model` varchar(50) NOT NULL,
  `price` int NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of phones
-- ----------------------------
BEGIN;
INSERT INTO `phones` (`id`, `brand`, `model`, `price`) VALUES (1, 'Apple', 'iPhone 14 Pro Max', 8999);
INSERT INTO `phones` (`id`, `brand`, `model`, `price`) VALUES (2, 'HUAWEI', 'HUAWEI Mate 50 Pro', 8399);
INSERT INTO `phones` (`id`, `brand`, `model`, `price`) VALUES (3, 'xiaomi', 'xiaomi 13 Ultra', 6799);
INSERT INTO `phones` (`id`, `brand`, `model`, `price`) VALUES (4, 'vivo', 'vivo X90 Pro', 6499);
INSERT INTO `phones` (`id`, `brand`, `model`, `price`) VALUES (5, 'OPPO', 'OPPO Find X6 Pro', 1111);
COMMIT;

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `password` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- ----------------------------
-- Records of users
-- ----------------------------
BEGIN;
INSERT INTO `users` (`id`, `username`, `password`) VALUES (1, 'zjj', '123');
INSERT INTO `users` (`id`, `username`, `password`) VALUES (2, '123', '123');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
