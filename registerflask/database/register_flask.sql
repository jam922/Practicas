-- phpMyAdmin SQL Dump
-- version 5.1.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 01-04-2022 a las 11:08:51
-- Versión del servidor: 10.4.21-MariaDB
-- Versión de PHP: 8.0.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `register_flask`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(255) NOT NULL,
  `password` varchar(255) NOT NULL,
  `fecha_creacion` date NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fecha_creacion`) VALUES
(1, 'juan', '202cb962ac59075b964b07152d234b70', '2022-04-01'),
(4, 'nuevo', 'pbkdf2:sha256:260000$h85EeCf2bUhEMhij$9b153e1333e12f24d657062f289f7c90ba70eb2e1814e4a37d9fe9da63d2b02e', '2022-04-01'),
(5, 'rfr', 'pbkdf2:sha256:260000$qybHEDs5ULYYkIyK$b61d4a8634946881057485d3433e7912a4ffc49165cd8d03b09f10f6c1dcaad4', '2022-04-01'),
(6, 'rfr', 'pbkdf2:sha256:260000$cVivKDSC3SsGastI$c79529c235436550f6246fe1851be1b008085097e594ce6c91c55ebe65e566d2', '2022-04-01'),
(7, 'rfr', 'pbkdf2:sha256:260000$3wJCx0kwK0jowiCB$ca31fac66253d8648ef602e3d546cb012c8e039c19a81d112444aa4f7ece31a3', '2022-04-01'),
(8, 'wkdwd', 'pbkdf2:sha256:260000$zaWgY1w0dz9Kcii6$776d64726130e0183f232b3bacb65bdcc44b96a4146f421ddc7ba25300511ccb', '2022-04-01'),
(9, 'usuarios', 'pbkdf2:sha256:260000$16zjHc21YD3xYqOI$99c9727f0825fc62aa933e6da69e8cdbaf47b3f9ba1b5732d0ed2b14586dd9fc', '2022-04-01'),
(10, 'nevo', 'pbkdf2:sha256:260000$IisQSqHBQYA76ant$32c7e8533f7c55fc47378f667c0047354a6f22bd1b28f4dbe011d1c4755211e7', '2022-04-01'),
(11, '', 'pbkdf2:sha256:260000$psFGFMHNx4lmPSFS$ef17f483675747b0021341076f8114469995875bd17a3a6ad31530d577e32dd6', '2022-04-01'),
(12, '', 'pbkdf2:sha256:260000$MjD63zlmfGYIePyw$e72c497ce27bf70338a3810ef012a81761a1548f67df231ed5bb2009a3e32b43', '2022-04-01'),
(13, 'OGARCIA', 'pbkdf2:sha256:260000$nywsI5y6hZsjY0Ln$525ac2e2a71e44f1a2ce478a1eb93c72eab2a11a03dae4769c5a5e91e46db8a8', '2022-04-01'),
(14, 'OGARCIA', 'pbkdf2:sha256:260000$acOHCcvsIKPwcpYl$3da95ac7c507e6391b1ec1274bba009a3af7b2f37d67c904362701e26d17c810', '2022-04-01'),
(15, '', 'pbkdf2:sha256:260000$crCwjdXwLhTYeMws$c07b0906ca63706edf7ae7d1efab136cc0a755774dfb3f4e5ce05f5b115fd76f', '2022-04-01'),
(16, 'hbbhh', 'pbkdf2:sha256:260000$7I4uusrU6dugSBan$b15ba7fcc6069e07138199350ae3f89e54d69381db84df492e5f565f44a41815', '2022-04-01'),
(17, 'nuevo', 'pbkdf2:sha256:260000$cvZgZacKerQEPUis$3d5c6431110c37bddfa5d3fdd20c24b918c1f797bb6f4653493d7118cd3b4495', '2022-04-01'),
(18, 'hbbhh', 'pbkdf2:sha256:260000$0aVGEMLo5K1cQQRZ$ea8c83c0ccecf01e2858d57bd67900946474f2c992af8c161c357a23514eb40b', '2022-04-01'),
(19, 'nuevo', 'pbkdf2:sha256:260000$uUZ60K4uOPd6CGkw$e9f556d8998addfa176421a06cd7ae29461fd6ab2964ad74621ee18ca3ffebcf', '2022-04-01'),
(20, '', 'pbkdf2:sha256:260000$Rk9D7BNaNgVDUqCi$d0f07af6dd77ec0c2c6adedc98894a2be757e3b684ae423217d0a9dfeccadf61', '2022-04-01');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
