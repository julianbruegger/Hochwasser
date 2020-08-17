<h1>Wasserstand - Bach Widacher</h1>

<?php
$servername = "192.168.111.61";
$username = "root";
$password = "***";
$dbname = "bach";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}

$sql = "SELECT time, distanz, up FROM wasser";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
  // output data of each row
  while($row = $result->fetch_assoc()) {
    echo "time: " . $row["time"]. " - Name: " . $row["distanz"]. " " . $row["up"]. "<br>";
  }
} else {
  echo "0 results";
}
$conn->close();
?>