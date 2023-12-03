import React from "react";
import "./SearchPage.css";
import useGoogleSearch from "../useGoogleSearch";
import useCustomSearch from "../useCustomSearch";
import { useStateValue } from "../StateProvider";
import Response from "../response";
import ResponseImage from "../responseImage";
import ResponseVideo from "../responseVideo";
import { Link } from "react-router-dom";
import Search from "../components/Search";
import SearchIcon from "@material-ui/icons/Search";
import mmse from './mmse1.jpg';
import DescriptionIcon from "@material-ui/icons/Description";
import ImageIcon from "@material-ui/icons/Image";
import LocalOfferIcon from "@material-ui/icons/LocalOffer";
import MoreVertIcon from "@material-ui/icons/MoreVert";
import RoomIcon from "@material-ui/icons/Room";

function SearchPage() {
  const [{ term }, dispatch] = useStateValue();

  //LIVE API CALL
 const { data } = useGoogleSearch(term);

  // MOCK API CALL
    //const data = Response;
    //const data = ResponseImage;
   // const data = ResponseVideo;

  //CUSTOM API CALL
   //   const { data } = useCustomSearch(term);

  console.log(data);
  return (
    <div className="searchPage">
      <div className="searchPage__header">
        <Link to="/">
          <img
            className="searchPage__logo"
            src={mmse}
            alt="multimodalsearchengine"
          />
        </Link>
        <div className="searchPage__headerBody">
          <Search hideButtons />

          <div className="searchPage_options">
            <div className="searchPage_optionsLeft">
              <div className="searchPage_option">
                <SearchIcon />
                <Link to="/all">All</Link>
              </div>
              <div className="searchPage_option">
                <DescriptionIcon />
                <Link to="/text">Text</Link>
              </div>
              <div className="searchPage_option">
                <ImageIcon />
                <Link to="/images">Images</Link>
              </div>
              <div className="searchPage_option">
                <LocalOfferIcon />
                <Link to="/audios">Vidoes</Link>
              </div>
              <div className="searchPage_option">
                <MoreVertIcon />
                <Link to="/more">More</Link>
              </div>
            </div>

          <div className="searchPage_optionsRight">
             {/* 
              <div className="searchPage_option">
                <Link to="/settings">Settings</Link>
              </div>
              <div className="searchPage_option">
                <Link to="/tools">Tools</Link>
              </div>
                */}
            </div>

          </div>
        </div>
      </div>
      {term && (
        <div className="searchPage__results">
         {/* <p className="searchPage__resultCount">
            About {data?.searchInformation.formattedTotalResults} results (
            {data?.searchInformation.formattedSearchTime} seconds) for {term}

          </p>
            */}
           <p className="searchPage__resultCount">
            Results obtained in (
            {data?.searchInformation.formattedSearchTime} seconds) for {term}

          </p>
          {data ?.items.map((item) => (
            <div className="searchPage__result">
              <a href={item.link}>
                {item.pagemap?.cse_image?.length > 0 &&
                  item.pagemap?.cse_image[0]?.src && (
                    <img
                      className="searchPage__resultImage"
                      src={item.pagemap?.cse_image[0]?.src}
                      alt=""
                    />
                  )}
                {item.displayLink}
              </a>
              <a className="searchPage__resultTitle" href={item.link}>
                <h2>{item.title}</h2>
              </a>
              <p className="searchPage__resultSnippet">{item.snippet}</p>
            </div>
          )
          )
                  
               /* Pages end 
               
        
          
     {data?.items.map((item) => (
            <div className="searchImage__result">
              <a href={item.link}>
                {item.pagemap?.cse_image?.length > 0 &&
                  item.pagemap?.cse_image[0]?.src && (
                    <img
                      className="searchImage__resultImage"
                      src={item.pagemap?.cse_image[0]?.src}
                      alt=""
                    />
                  )}<br/>
                {item.displayLink}
              </a>
              <a className="searchImage__resultTitle" href={item.link}>
                <h2>{item.title}</h2>
              </a>
              <p className="searchPage__resultSnippet">{item.snippet}</p>
            </div>
          )
          )
            /*Images end */
        }  
        

        
     {/*   
     {data?.items.map((item) => (
     
     <div className="searchVideo__result"><br/> 
          <a className="searchVideo__resultTitle" href={item.link}>
          {item.displayLink}
          <h2>{item.title}</h2>
        </a>
        <p className="searchPage__resultSnippet">{item.snippet}</p>
        <a href={item.link}>
          {item.pagemap?.cse_image?.length > 0 &&
            item.pagemap?.cse_image[0]?.src && (
              <img
                className="searchVideo__resultImage"
                src={item.pagemap?.cse_image[0]?.src}
                alt=""
              />
            )}<br/>
          
        </a>
      </div>
    )
    )
      /*Video end */  

     /* No data 
     { ! noData => (
        <div className="searchPage__result">
          NO RESULT FOUND !
        </div>
      )
              )*/}

               
        </div>
      )}
    </div>
  );
}

export default SearchPage;
