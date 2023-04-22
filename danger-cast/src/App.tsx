import React, { useRef, useEffect } from "react";
import L from "leaflet";

import "leaflet/dist/leaflet.css";
import "./App.css";

const Map: React.FC = () => {
  const mapRef = useRef<HTMLDivElement>(null);
  const boxRef = useRef<HTMLDivElement>(null);
  const lisbonMarkerRef = useRef<L.Marker | null>(null);
  const portoMarkerRef = useRef<L.Marker | null>(null);

  useEffect(() => {
    if (mapRef.current && boxRef.current) {
      // create map instance
      const map = L.map(mapRef.current).setView([39.5, -8], 7);

      // add tile layer
      L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
        attribution: "Map data &copy; OpenStreetMap contributors",
      }).addTo(map);

      // add markers
      const lisbonMarker = L.marker([38.7223, -9.1393]).addTo(map);
      const portoMarker = L.marker([41.1579, -8.6291]).addTo(map);
      
      // store marker references
      lisbonMarkerRef.current = lisbonMarker;
      portoMarkerRef.current = portoMarker;

      // add popups to markers
      lisbonMarker
        .bindPopup("Lisbon")
        .on("click", () => console.log("Lisbon marker clicked"));
      portoMarker
        .bindPopup("Porto")
        .on("click", () => console.log("Porto marker clicked"));

      // update box position when map is moved
      map.on("move", () => {
        if (boxRef.current && lisbonMarkerRef.current && portoMarkerRef.current) {
          const lisbonPos = map.latLngToContainerPoint(lisbonMarkerRef.current.getLatLng());
          const portoPos = map.latLngToContainerPoint(portoMarkerRef.current.getLatLng());
          const top = Math.min(lisbonPos.y, portoPos.y);
          const left = Math.min(lisbonPos.x, portoPos.x);
          const bottom = Math.max(lisbonPos.y, portoPos.y);
          boxRef.current.style.top = top + "px";
          boxRef.current.style.left = left + "px";
          boxRef.current.style.bottom = (map.getSize().y - bottom) + "px";
        }
      });

      // set bounds to show only Portugal
      const southWest = L.latLng(36.838, -9.526);
      const northEast = L.latLng(42.282, -6.189);
      const bounds = L.latLngBounds(southWest, northEast);
      map.fitBounds(bounds);
    }
  }, []);

  return (
    <div className="map-container">
      <div ref={mapRef} className="map" />
      <div ref={boxRef} className="box">
        <p>Information Box</p>
        <p>This is some text in the information box.</p>
      </div>
    </div>
  );
};

export default Map;
