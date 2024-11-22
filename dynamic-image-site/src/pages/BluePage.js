import React from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";

const PageContainer = styled.div`
  text-align: center;
  min-height: 100vh;
  background-color: #0C4767;
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
  color: blue;
  cursor: pointer;
  transition: all 0.3s ease;

  &:hover {
    transform: scale(1.1);
    background-color: blue;
    color: white;
  }
`;

const BluePage = () => {
  const navigate = useNavigate();

  return (
    <PageContainer>
      <Title>Welcome to the red page</Title>
      <BackButton onClick={() => navigate("/")}>Back to Home</BackButton>
    </PageContainer>
  );
};

export default BluePage;

