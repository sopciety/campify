import React from "react";
import { useNavigate } from "react-router-dom";
import styled from "styled-components";


const PageContainer = styled.div`
  text-align: center;
  min-height: 100vh;
  background: linear-gradient(135deg, #0c4767, #063a4a);
  color: white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  font-family: "Inter", sans-serif;
  overflow: hidden; /* Prevent content overflow */
`;

const Title = styled.h1`
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 10px;
  letter-spacing: 2px;
  text-transform: uppercase;
  animation: fadeIn 2s ease-in-out;
  font-family: "jsMath-cmbx10", sans-serif;
  @keyframes fadeIn {
    0% {
      opacity: 0;
      transform: translateY(-20px);
    }
    100% {
      opacity: 1;
      transform: translateY(0);
    }
  }
`;

const SubTitle = styled.h2`
  font-size: 2rem;
  font-weight: 500;
  margin-bottom: 30px;
  opacity: 0.9;
  font-family: "jsMath-cmbx10", sans-serif;
`;

const BackButton = styled.button`
  padding: 12px 25px;
  font-size: 1rem;
  border: none;
  border-radius: 30px;
  background: linear-gradient(to right, #ff6b6b, #ff8787);
  color: white;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 4px 10px rgba(255, 107, 107, 0.3);
  font-family: "jsMath-cmbx10", sans-serif;

  &:hover {
    transform: scale(1.1);
    box-shadow: 0 6px 15px rgba(255, 107, 107, 0.5);
  }
`;

const ImagesContainer = styled.div`
  display: flex;
  justify-content: center;
  gap: 30px; /* Increased spacing */
  margin-top: 20px;
  flex-wrap: wrap; /* Wrap images on smaller screens */
`;

const StyledImage = styled.img`
  width: 160px;
  height: auto;
  border-radius: 15px;
  box-shadow: 0 6px 10px rgba(0, 0, 0, 0.3);
  transition: transform 0.3s ease, box-shadow 0.3s ease;

  &:hover {
    transform: scale(1.1);
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.5);
  }
`;

const StyledAsset = styled.img`
  width: 150px; /* Set a uniform width */
  height: auto; /* Maintain aspect ratio */
  border-radius: 10px; /* Optional: add rounded corners */
  
`;


const LandscapeContainer = styled.div`
  position: relative;
  width: 100%;
  height: 300px;
  margin-top: 40px;
  background: linear-gradient(to top, #3b5f3c, transparent);
  display: flex;
  justify-content: center;
  align-items: flex-end;
  overflow: hidden;
`;


const RedPage = () => {
  const navigate = useNavigate();

  return (
    <PageContainer>
      <Title>Campify</Title>
      <SubTitle>Top 3 Artists</SubTitle>
      <ImagesContainer>
        <StyledImage src="/album1.png" alt="Laufey" />
        <StyledImage src="/album2.png" alt="KPOP" />
        <StyledImage src="/album3.png" alt="BMars" />
      </ImagesContainer>
      <LandscapeContainer>
      <ImagesContainer>
        <StyledAsset src="/tree.png" alt="Tree" />
        <StyledAsset src="/campfire.png" alt="Campfire" />
        <StyledAsset src="/tent_asset.png" alt="Tent" />
      </ImagesContainer>
      </LandscapeContainer>
      <BackButton onClick={() => navigate("/")}>Back to Home</BackButton>
    </PageContainer>
  );
};

export default RedPage;