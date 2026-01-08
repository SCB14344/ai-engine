<?php
$input = json_decode(file_get_contents("php://input"), true);

$data = json_encode(["input" => $input["message"]]);

$context = stream_context_create([
  "http" => [
    "method" => "POST",
    "header" => "Content-Type: application/json",
    "content" => $data
  ]
]);

$response = file_get_contents("http://localhost:8000/infer", false, $context);
echo $response;