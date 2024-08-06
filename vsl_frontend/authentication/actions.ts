"use server";

import { cookies } from "next/headers";
import { jwtDecode } from "jwt-decode";
import { ACCESS_TOKEN, REFRESH_TOKEN } from "./token";

export async function setToken(access: string, refresh: string) {
    const decodedAccessToken = jwtDecode<{ exp: number }>(access);
    const accessTokenExpiration: number = decodedAccessToken.exp;
    const decodedRefreshToken = jwtDecode<{ exp: number }>(refresh);
    const refreshTokenExpiration: number = decodedRefreshToken.exp;

    cookies().set(ACCESS_TOKEN, access, {
        expires: accessTokenExpiration * 1000,
        httpOnly: true,
        secure: true,
    });
    cookies().set(REFRESH_TOKEN, refresh, {
        expires: refreshTokenExpiration * 1000,
        httpOnly: true,
        secure: true,
    });
}

export async function getAccessToken() {
    const accessToken = cookies().get(ACCESS_TOKEN);
    return accessToken?.value;
}

export async function getRefreshToken() {
    const refreshToken = cookies().get(REFRESH_TOKEN);
    return refreshToken?.value;
}

export async function deleteTokens() {
    cookies().delete(ACCESS_TOKEN);
    cookies().delete(REFRESH_TOKEN);
}

export async function hasTokens() {
    console.log(cookies().has(ACCESS_TOKEN));
    return cookies().has(ACCESS_TOKEN);
}
