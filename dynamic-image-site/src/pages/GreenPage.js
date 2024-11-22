import React from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";

const PageContainer = styled.div`
  text-align: center;
  min-height: 100vh;
  background-color: green;
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Inter", sans-serif;
`;

const Title = styled.h1`
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 20px;
`;

const BackButton = styled.button`
  padding: 10px 20px;
  font-size: 1rem;
  border: none;
  border-radius: 5px;
  background-color: white;
  color: #ff6b6b;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    transform: scale(1.1);
    background-color: #ff8787;
    color: white;
  }
`;

const GreenPage = () => {
  const navigate = useNavigate();

  return (
    <PageContainer>
      <Title>Welcome to the green page</Title>
      <BackButton onClick={() => navigate("/")}>Back to Home</BackButton>
    </PageContainer>
  );
};

export default GreenPage;
